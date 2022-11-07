from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'auteur': 'Romain N.',
        'title': 'Blog post 1',
        'content': 'This is the first blog content',
        'date_posted': '7/11/2022'
    },
    {
        'auteur': 'Romain N.',
        'title': 'Blog post 2',
        'content': 'This is the second blog content',
        'date_posted': '8/11/2022'
    }
]

def blog_home(request):
    #return HttpResponse('<h1>Welcome to the Blog Homepage</h1>')
    context = {
        'posts': posts,
    }
    return render(request,'my_blog/home.html', context)

def blog_about(request):
    #return HttpResponse('<h1>about page</h1>')
    return render(request,'my_blog/about.html',{'title':'About'})
