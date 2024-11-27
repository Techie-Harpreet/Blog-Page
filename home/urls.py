from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', home , name="home"),
    path('contact-us', contact_us, name="contact-us"),
    path('about-us', about_us, name="about-us"),


]
