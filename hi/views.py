from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from datetime import datetime
# Create your views here.


def home(request):
    blogss = Blog.objects
    return render(request, 'home.html', {'blogs': blogss})


def detail(request, blog_id):
    blogs = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'blog':blogs})


def send(request):
   
    return render(request, 'send.html' )

def create(request):

    blog=Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/')



