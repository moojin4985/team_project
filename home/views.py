from django.shortcuts import render, loader

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import Post, Support


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
    if request.method == 'POST':
        new_supporter = Support.objects.create(
            name = request.POST['name'],
            phone_number = request.POST['phone_number'],
            email = request.POST['email'],
            contents = request.POST['contents'],
        ) 
        return HttpResponseRedirect('/home/support')
    return render(request, "support.html")


def team(request):
    return render(request, "team.html")


def event(request):
    return render(request, "event.html")


def map(request):
    return render(request, "map.html")

#@csrf_exempt
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
    
    supportCount = Support.object.count()
    
    if search_option == 'writer': 
        Searchlist = Support.object.filter( Q(name__contains = search)).order_by('-idx')
    elif search_option == 'phonenum': 
        Searchlist = Support.object.filter( Q(phonenum__contains = search)).order_by('-idx')
    elif search_option == 'email': 
        Searchlist = Support.object.filter( Q(email__contains = search)).order_by('-idx')
    
    supportlist = Post.objects.order_by('-idx') 
    
    postlist = Post.objects.all()
    supportall = Support.objects.all()
    return render(request, "board.html", {'postlist': postlist, 'supportall':supportall, 'supportlist': supportlist, 
                                            'supportCount':supportCount, 'search_option':search_option, 'search':search})


def viewboard(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "viewboard.html", {'post': post})

