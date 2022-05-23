import datetime
from django.db import models
from django.utils import timezone
from datetime import date


class Category(models.Model):
    name = models.CharField("Category", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = "Category"


class Genre(models.Model):
    name = models.CharField("Name", max_length=100)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Actor(models.Model):
    name = models.CharField("Name", max_length=150)
    age = models.PositiveIntegerField("Age", default=0)
    imageURL = models.ImageField("Image", upload_to="actors/")
    description = models.TextField("Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"


class Movie(models.Model):
    title = models.CharField("Name", max_length=100)
    description = models.CharField("Description", max_length=300)
    imageURL = models.ImageField("Poster", upload_to="movies/")
    date_of_release = models.DateField("release date", default=date.today)
    producers = models.ManyToManyField(Actor, verbose_name="producer", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="actor", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Genres")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class Member(models.Model):
    member_name = models.CharField(max_length=100, verbose_name="Name")
    email_address = models.CharField(max_length=100, verbose_name="Email Address", null=True, unique=True)
    age = models.PositiveIntegerField(verbose_name="Age", null=True)
    birthday = models.DateTimeField(null=True)
    gender = models.CharField(max_length=100, null=True)
    member_join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member_name


class MoviePictures(models.Model):
    title = models.CharField("Title", max_length=200)
    image = models.ImageField("Pictures", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="movie", on_delete=models.CASCADE) #если удалить фильм, то за ним и все изображения

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie picture"
        verbose_name_plural = "Movie pictures"


class StarRate(models.Model):
    amount = models.PositiveSmallIntegerField("Amount", default=0)

    def __str__(self):
        return self.amount

    class Meta:
        verbose_name = "Star"
        verbose_name_plural = "Stars"


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="movie")
    rate = models.ForeignKey(StarRate, on_delete=models.CASCADE, verbose_name="rate")

    def __str__(self):
        return f"{self.rate} - {self.movie}"

    class Meta:
        verbose_name = "rating"

