from django.conf import settings
from django.db import models
from django.shortcuts import redirect
from django.views.generic.base import View
from django.shortcuts import render
from .models import Movie, Member
from . import forms


def get_movie_by_id(id):
    try:
        movie = Movie.objects.get(id=id)
        return movie
    except:
        return None

def get_member_by_id(id):
    try:
        member = Member.objects.get(id=id)
        return member
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


class MovieRentalView(View):
    def get(self, request):
        if request.method == "GET":
            rent_form = forms.MovieRentalForm()
            return render(request, 'movies/rent_movie.html', {"rent_form": rent_form})

    def post(self, request):
        if request.method == "POST":
            rent_form = forms.MovieRentalForm(request.POST)
            if rent_form.is_valid():
                rent_form.save()
                success = {"strong": "Have a nice day bro!"}
                return render(request, "movies/order_success.html", {"success": success})
            return render(request, "movies/rent_movie.html", {"rent_form": rent_form})
        rent_form = forms.MovieRentalForm()
        return render(request, 'movies/rent_movie.html', {"rent_form": rent_form})


class MemberRentalInfoView(View):
    def get(self, request):
        members = Member.objects.all()
        return render(request, 'movies/member_rental_info.html', {"members": members, "data": None})

    def post(self, request):
        members = Member.objects.all()
        if request.method == "POST":
            member_id = int(request.POST.get("member"))
            if member_id:
                selected_member = members.get(id=member_id)
                return render(request, 'movies/member_rental_info.html',
                              {"members": members, "data": selected_member, "selected_value": member_id})
        members = Member.objects.all()
        return render(request, 'movies/member_rental_info.html', {"members": members, "data": None})

