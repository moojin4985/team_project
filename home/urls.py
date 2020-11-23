from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings


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
    path('board/', views.board),
    path('board/<int:pk>/', views.viewboard, name='viewboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)