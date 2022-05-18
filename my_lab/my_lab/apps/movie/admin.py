from django.contrib import admin
from .models import Movie, Comment, Member

admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Member)
