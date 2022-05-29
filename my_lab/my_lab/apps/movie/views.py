from django.conf import settings
from django.db import models
from django.shortcuts import redirect
from django.views.generic.base import View
from django.shortcuts import render
from .models import Movie, Member, Actor
from . import forms
from django.db.models import Q


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

def get_actor_by_id(id):
    try:
        actor = Actor.objects.get(id=id)
        return actor
    except:
        return None


class MoviesView(View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            movies = Movie.objects.filter(Q(title__icontains=search_query))
        else:
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


class MovieCreateView(View):
    def get(self, request):
        form = forms.MovieForm()
        return render(request, 'movies/movie_create.html', {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = forms.MovieForm(request.POST, request.FILES)
            if form.is_valid():
                name = form.cleaned_data['title']
                form.imageURL = form.cleaned_data
                form.save()
                data = {"strong": f"Movie with name {name.title()} created", "simple": "this movie can now be rented"}
                return render(request, 'movies/movie_creation_success.html', {"data": data})
            return render(request, 'movies/movie_create.html', {"form": form})


class MovieUpdateView(View):
    def get(self, request, id):
        form = forms.MovieForm()
        return render(request, 'movies/movie_update.html', {'movie': get_movie_by_id(id), 'form': form})

    def post(self, request, id):
        form = forms.MovieForm(request.POST, instance=get_movie_by_id(id))
        if form.is_valid():
            form.save()
            return redirect('/movies/')


class MovieDeleteView(View):
    def get(self, request, id):
        return render(request, 'movies/movie_delete.html', {'movie': get_movie_by_id(id)})

    def post(self, request, id):
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/movies/')


class MemberUpdateView(View):
    def get(self, request, id):
        form = forms.MemberForm()
        return render(request, 'movies/member_update.html', {'member': get_member_by_id(id), 'form': form})

    def post(self, request, id):
        form = forms.MemberForm(request.POST or None, instance=get_member_by_id(id))
        if form.is_valid():
            form.save()
            return redirect('/members/')


class MemberDeleteView(View):
    def get(self, request, id):
        return render(request, 'movies/member_delete.html', {'member': get_member_by_id(id)})

    def post(self, request, id):
        member = Member.objects.get(id=id)
        member.delete()
        return redirect('/members/')


class MemberCreateView(View):
    def get(self, request):
        form = forms.MemberForm()
        return render(request, 'movies/member_create.html', {'form': form})

    def post(self, request):
        form = forms.MemberForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['member_name']
            form.save()
            data = {"strong": f"Member with name {name.title()} created", "simple": "you can now start renting movies"}
            return render(request, 'movies/movie_creation_success.html', {"data": data})
        return render(request, 'movies/member_create.html', {"form": form})


class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        return render(request, 'movies/actor_index.html', {"actor_list": actors})


class ActorCreateView(View):
    def get(self, request):
        form = forms.ActorForm()
        return render(request, 'movies/actor_create.html', {'form': form})

    def post(self, request):
        form = forms.ActorForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            data = {"strong": f"Actor with name {name.title()} created"}
            return render(request, 'movies/movie_creation_success.html', {'data': data})
        return render(request, 'movies/actor_create.html', {'form': form})


class ActorDeleteView(View):
    def get(self, request, id):
        return render(request, 'movies/actor_delete.html', {'actor': get_actor_by_id(id)})

    def post(self, request, id):
        actor = Actor.objects.get(id=id)
        actor.delete()
        return redirect('/actors/')


class ActorUpdateView(View):
    def get(self, request, id):
        form = forms.ActorForm()
        return render(request, 'movies/actor_update.html', {'actor': get_actor_by_id(id), 'form': form})

    def post(self, request, id):
        form = forms.ActorForm(request.POST, instance=get_actor_by_id(id))
        if form.is_valid():
            form.save()
            return redirect('/actors/')


