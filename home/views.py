from django.shortcuts import render, loader

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import News, Post


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


# def news(request):
#    return render(request, "news.html")

def news(request):
    newslist = News.objects.all()
    return render(request, "news.html", {'newslist':newslist})


def support(request):
    return render(request, "support.html")


def team(request):
    return render(request, "team.html")


def event(request):
    return render(request, "event.html")


def map(request):
    return render(request, "map.html")

"""
def board(request):
    
    # 검색기능
    try:
        search_option = request.POST['search_option']
    except:
        search_option = 'writer'
    try:
        search = request.POST['search']
    except:
        search = ''    
    
    supportCount = Support.objects.count()
    
    if search_option == 'writer': 
        Searchlist = Support.objects.filter( Q(name__contains = search)).order_by('-idx')
    elif search_option == 'phone_number': 
        Searchlist = Support.objects.filter( Q(phone_number__contains = search)).order_by('-idx')
    elif search_option == 'email': 
        Searchlist = Support.objects.filter( Q(email__contains = search)).order_by('-idx')
    
    supportlist = Post.objects.all().order_by('-id') 
    'supportlist': supportlist, 'supportCount':supportCount, 'search_option':search_option, 'search':search
    

    postlist = Post.objects.all()
    #supportall = Support.objects.all() 'supportall':supportall, 
    return render(request, "board.html", {'postlist': postlist})


def viewboard(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "viewboard.html", {'post': post})
"""

