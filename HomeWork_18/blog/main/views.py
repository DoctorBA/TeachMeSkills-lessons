from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    posts = Post.objects.all()
    return  render(request, 'home.html', context={'posts':posts})


def about(request):
    return render(request, 'about.html')
