import datetime
from django.db import models
from cloudinary.models import CloudinaryField
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


class Actor(models.Model):
    name = models.CharField("Name", max_length=150)
    age = models.PositiveIntegerField("Age", default=0)
    imageURL = CloudinaryField("imageURL")
    description = models.TextField("Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"


class Movie(models.Model):
    title = models.CharField("Name", max_length=100)
    description = models.CharField("Description", max_length=300)
    genre = models.CharField(max_length=100, default="genre")
    imageURL = CloudinaryField("imageURL", null=True, blank=True)
    date_of_release = models.DateField("release date", default=date.today)
    actors = models.ManyToManyField(Actor, verbose_name="actor", related_name="film_actor")
    price = models.PositiveIntegerField(default=100)
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


class MovieRental(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="Member Name")
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Movie Name")
    rent_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()


class Producer(models.Model):
    producer_name = models.CharField(max_length=100, verbose_name="Name")
    age = models.PositiveIntegerField("Age", default=0)
    imageURL = models.ImageField("Image", upload_to="producers/")
    Biography = models.TextField("Bio")

    def __str__(self):
        return self.producer_name

    class Meta:
        verbose_name = "Producer"
        verbose_name_plural = "Producers"



