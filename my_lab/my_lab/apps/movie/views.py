from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request, 'main/index.html', {'title': 'Movies today: ', 'list': movies})

def test(request):
    return HttpResponse('Test')

def check_movie(request):
    return render(request, 'main/check_movie.html')
