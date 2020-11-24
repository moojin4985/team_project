from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('establish', views.establish, name='establish'),
    path('business', views.business, name='business'),
    path('activity', views.activity, name='activity'),
    path('scontent', views.scontent, name='scontent'),
    path('news', views.news, name='news'),
    path('support', views.support, name='support'),
    path('team', views.team, name='team'),
    path('event', views.event, name='event'),
    path('map', views.map, name='map'),
    path('board/', views.board, name='board'),
    path('board/<int:pk>/', views.viewboard, name='viewboard'),
    path('board/newpost/', views.newpost, name='newpost'),
]