from django.shortcuts import render, redirect,get_object_or_404
from .models import Blog

# Create your views here.


def IndexPage(request):
    blogs = Blog.objects.all()

    return render(request, 'blogApp/index.html',{'blogs':blogs})


def BlogPage(request):
    blogs = Blog.objects.all()
    return render(request, 'blogApp/blog.html',{'blogs':blogs})


def PostPage(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogApp/post.html',{'blog':blog})


