from django.conf import settings
from django.db import models
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.shortcuts import render
from .models import Movie, Member


def get_movie_by_id(id):
    try:
        movie = Movie.objects.get(id=id)
        return movie
    except:
        return None


class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movies/movie_index.html", {"movie_list": movies})


class RentView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/rent_index.html', {"data": movies})


class MovieDetailView(View):
    def get(self, request, id):
        return render(request, "movies/details.html", {"movie": get_movie_by_id(id)})


class MembersView(View):
    def get(self, request):
        members = Member.objects.all()
        return render(request, 'movies/member_index.html', {"data": members})
