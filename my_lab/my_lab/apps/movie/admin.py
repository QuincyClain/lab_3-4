from django.contrib import admin
from .models import Movie, Member, Category, Actor

admin.site.register(Movie)
admin.site.register(Member)
admin.site.register(Category)
admin.site.register(Actor)

