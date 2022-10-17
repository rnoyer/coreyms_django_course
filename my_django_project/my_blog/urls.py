from django.contrib import admin
from django.urls import include, path

from my_blog import views

urlpatterns = [
    path('',views.blog_home,name='blog_homepage'),
    path('about/',views.blog_about,name='blog_about')
]
