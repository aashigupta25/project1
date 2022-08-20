from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path("", views.index, name='home'),
    path("About", views.About, name='About'),
    path("Service", views.Service, name='Service'),
    path("Contact", views.Contact, name='Contact'),
    path("Blog", views.Blog, name='Blog')
    

]