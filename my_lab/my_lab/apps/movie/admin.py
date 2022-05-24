from django.contrib import admin
from .models import Movie, Member, Category, Actor, MovieRental

admin.site.register(Movie)
admin.site.register(Member)
admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(MovieRental)
