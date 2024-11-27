from django.shortcuts import render,redirect
from blog.models import Category,BlogPost,HomeSlider
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from blog.models import Contact

def home(request):

    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']

        user = User.objects.create_user(email, password)
        user.save()
        return HttpResponseRedirect(request.path_info)

    category = Category.objects.all()
    blogpost = BlogPost.objects.all()
    category2 = Category.objects.all().order_by('cat_id')[0:3]
    homeslider = HomeSlider.objects.all()


    context = {
        'category' : category,
        'blogpost' : blogpost,
        'category2' : category2,
        'homeslider' : homeslider
    }
    return render(request , "pages/index.html",context)


def contact_us(request):
    if request.method=="POST":
        email=request.POST['email']
        content =request.POST['content']
       
        contact_form=Contact(email=email,content=content)
        contact_form.save()
        messages.success(request, "Your message has been successfully sent")
        return render(request, "alert/contact-us.html")
    category = Category.objects.all()

    context = {
        'category' : category
    }
    return render(request, 'pages/contact.html',context)

def about_us(request):
    category = Category.objects.all()

    context = {
        'category' : category
    }
    return render(request, 'pages/about.html',context)


