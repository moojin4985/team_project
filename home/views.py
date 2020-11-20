from django.shortcuts import render, loader

# Create your views here.
from django.http import HttpResponse
from .models import Post


def home(request):
    return render(request, "base.html")

def team(request):
    return render(request, "team.html")


def board(request):
    postlist = Post.objects.all()
    return render(request, "board.html", {'postlist': postlist})