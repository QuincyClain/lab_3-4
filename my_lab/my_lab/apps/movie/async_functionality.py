from .models import Movie, Member, Actor
from asgiref.sync import sync_to_async
from django.db.models import Q


@sync_to_async
def get_movie_by_id(id):
    try:
        movie = Movie.objects.get(id=id)
        return movie
    except:
        return None


@sync_to_async
def get_member_by_id(id):
    try:
        member = Member.objects.get(id=id)
        return member
    except:
        return None


@sync_to_async
def get_actor_by_id(id):
    try:
        actor = Actor.objects.get(id=id)
        return actor
    except:
        return None


@sync_to_async
def get_all_movies():
    movies = Movie.objects.all()
    return movies


@sync_to_async
def get_filtered_movies(search_query):
    filtered_movies = Movie.objects.filter(Q(title__icontains=search_query))
    return filtered_movies


@sync_to_async
def get_all_members():
    members = Member.objects.all()
    return members


@sync_to_async
def get_all_actors():
    actors = Actor.objects.all()
    return actors