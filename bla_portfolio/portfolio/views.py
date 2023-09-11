from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.forms import UploadForm
from portfolio.models import Blogs
from django.db import models

# from django.conf import settings


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')


def addBlog(request): 
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    return render(request, 'addBlog.html',{'form' : UploadForm})


def services(request):
    return render(request, 'services.html')

def resume(request):
    return render(request, 'resume.html')

def blog(request):
    posts = Blogs.objects.all()
    context = {"posts": posts}
    return render(request, 'blog.html', context)


