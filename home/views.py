from django.shortcuts import render, loader

# Create your views here.
from django.http import HttpResponse
from .models import Post


def home(request):
    return render(request, "home/main.html")


def board(request):
    postlist = Post.objects.all()
    return render(request, "home/home.html", {'postlist': postlist})