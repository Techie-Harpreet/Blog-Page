from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [

    path('register', register_page, name="register_page"),
    path('login', login_page, name="handleLogin"),
    path('logout', handelLogout, name="handleLogout"),


]
