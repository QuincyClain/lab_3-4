from django.urls import path
from my_lab import settings
from . import views

urlpatterns = [
    path("", views.MoviesView.as_view())
]