from django.shortcuts import render, loader

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, "home/main.html")
