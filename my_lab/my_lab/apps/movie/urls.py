from django.urls import path
from my_lab import settings
from . import views

urlpatterns = [
    path("", views.RentView.as_view(), name="home"),
    path("movies/", views.MoviesView.as_view(), name="movie_views"),
    path("movies/details/<int:id>/", views.MovieDetailView.as_view()),
    path("members/", views.MembersView.as_view()),
    path("rent/", views.MovieRentalView.as_view()),
    path("rent/success", views.MoveRentalSuccessView.as_view()),
    path("member/rental", views.MemberRentalInfoView.as_view()),
    path("movie/create/", views.MovieCreateView.as_view()),
    path("movie/update/<int:id>/", views.MovieUpdateView.as_view()),
    path("movie/delete/<int:id>/", views.MovieDeleteView.as_view()),
    path("member/update/<int:id>/", views.MemberUpdateView.as_view()),
    path("member/delete/<int:id>/", views.MemberDeleteView.as_view()),
    path("member/create/", views.MemberCreateView.as_view()),
    path("actors/", views.ActorView.as_view()),
    path("actor/create/", views.ActorCreateView.as_view()),
    path("actor/delete/<int:id>/", views.ActorDeleteView.as_view()),
    path("actor/update/<int:id>/", views.ActorUpdateView.as_view()),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout")

]
