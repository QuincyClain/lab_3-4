from django.urls import path
from my_lab import settings
from . import views

urlpatterns = [
    path("", views.RentView.as_view()),
    path("movies/", views.MoviesView.as_view()),
    path("movies/details/<int:id>/", views.MovieDetailView.as_view()),
    path("members/", views.MembersView.as_view()),
    path("rent/", views.MovieRentalView.as_view()),
    path("member/rental", views.MemberRentalInfoView.as_view()),
]
