from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('establish', views.establish),
    path('business', views.business),
    path('activity', views.activity),
    path('scontent', views.scontent),
    path('news', views.news),
    path('support', views.support),
    path('team', views.team),
    path('event', views.event),
    path('map', views.map),
    path('board', views.board),
]