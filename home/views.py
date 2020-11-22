from django.shortcuts import render, loader

# Create your views here.
from django.http import HttpResponse
from .models import Post


def home(request):
    return render(request, "main.html")


def establish(request):
    return render(request, "establish.html")


def business(request):
    return render(request, "business.html")


def activity(request):
    return render(request, "activity.html")


def scontent(request):
    return render(request, "scontent.html")


def news(request):
    return render(request, "news.html")


def support(request):
    return render(request, "support.html")


def team(request):
    return render(request, "team.html")


def event(request):
    return render(request, "event.html")


def map(request):
    return render(request, "map.html")


def board(request):
    postlist = Post.objects.all()
    return render(request, "board.html", {'postlist': postlist})


def viewboard(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "viewboard.html", {'post': post})

