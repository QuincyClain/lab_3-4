from django.urls import path
from my_lab import settings
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('test/', views.test, name = 'test'),
    path('check_movie', views.check_movie, name = 'check_movie')
]