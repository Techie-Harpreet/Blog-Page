from django.shortcuts import render,redirect
from .models import Category,BlogPost,HomeSlider
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact

@login_required(login_url='/accounts/login')
def single_blog(request , slug):
    category = Category.objects.all()

    blogpost = BlogPost.objects.filter(slug = slug) 
    # blogpost2 = BlogPost.objects.all().order_by('id')[0:2]

    if blogpost.exists():
        blogpost = blogpost.first()
    
    else:
        return redirect("home")

    context = {
            'blogpost' : blogpost,
            'category' : category,
            # 'blogpost2' : blogpost2
            }
    return render(request , 'blog-pages/single-blog.html',context)


def Category_filter(request,id):
    category = Category.objects.all()
    blogpost_category = Category.objects.get(cat_id = id)
    blogpost = BlogPost.objects.filter(category_name = blogpost_category)
    context = {
        'blogpost_category' : blogpost_category,
        'blogpost' : blogpost,
        'category' : category
    }

    return render(request , 'blog-pages/filter-blog.html',context)


def search(request):
    category = Category.objects.all()
    query=request.GET['query']
    blogpost= BlogPost.objects.filter(title__icontains = query)
    context = {
        'blogpost' : blogpost,
        'category' : category
    }
    return render(request, 'blog-pages/search.html', context)


def All_Blog(request):
    category = Category.objects.all()
    blogpost = BlogPost.objects.all()

    context = {
        'blogpost' : blogpost,
        'category' : category
    }
    return render(request, 'blog-pages/all-blog.html', context)

