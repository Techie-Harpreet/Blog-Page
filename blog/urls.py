from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('blog', search, name="search"),
    path('<slug>/' , single_blog , name="single_blog"),
    path('blog/<int:id>/' , Category_filter , name="Category_filter"),
    path('all-blogs', All_Blog, name="all-blogs"),




]
