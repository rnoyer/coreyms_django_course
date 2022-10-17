from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def blog_home(request):
    return HttpResponse('<h1>Welcome to the Blog Homepage</h1>')

def blog_about(request):
    return HttpResponse('<h1>about page</h1>')
