from django.views.generic.base import View
from django.shortcuts import render
from .models import Movie


class MoviesView(View):
    #get request
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movie_index.html", {"movie_list": movies})