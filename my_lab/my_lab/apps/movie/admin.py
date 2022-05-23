from django.contrib import admin
from .models import Movie, Member, Genre, Category, MovieRating, StarRate, Actor, MoviePictures

admin.site.register(Movie)
admin.site.register(Member)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(MovieRating)
admin.site.register(StarRate)
admin.site.register(Actor)
admin.site.register(MoviePictures)
