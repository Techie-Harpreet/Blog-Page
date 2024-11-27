from django.db import models
from froala_editor.fields import FroalaField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from datetime import datetime





class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_img = models.ImageField(upload_to="Media/Author-img")
    def __str__(self):
        return self.author_name


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    icon = models.CharField(max_length=200,null=True,blank=True)
    category_name = models.CharField(max_length=200)

    def __str__(self):
          return self.category_name

class BlogPost(models.Model):
    slug = models.SlugField(unique=True , null=True , blank=True)
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="Media/blog-post-img")
    short_decription = models.TextField(max_length=200,null=True,blank=True)
    decription = FroalaField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)

    category_name = models.ForeignKey(Category,on_delete= models.CASCADE,null=True,blank=True)
    author = models.ForeignKey(Author,on_delete= models.CASCADE,null=True,blank=True)
    # category_name = models.ManyToManyField(Category)


    def __str__(self):
          return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("single_blog", kwargs={'slug': self.slug})




class HomeSlider(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    img = models.ImageField(upload_to="Media/Home-slider-img")
    description = models.TextField(max_length=500,null=True,blank=True)

    def __str__(self):
          return "Slider Images"


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = BlogPost.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, BlogPost)



class Contact(models.Model):
     
     email= models.CharField(max_length=100)
     content= models.TextField()


     def __str__(self):
          return "Message from " + self.email







