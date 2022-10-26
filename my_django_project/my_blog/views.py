from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog_home(request):
    #return HttpResponse('<h1>Welcome to the Blog Homepage</h1>')
    return render(request,'my_blog/home.html')

def blog_about(request):
    return HttpResponse('<h1>about page</h1>')
