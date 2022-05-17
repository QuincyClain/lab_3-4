import datetime
from django.db import models
from django.utils import timezone


# Create your models here.

class Movie(models.Model):
    movie_title = models.CharField('Movie name', max_length=200)
    # movie_images = models.ImageField(null=True, blank=True, upload_to="", verbose_name="Image")
    movie_description = models.TextField('Movie description')
    release_date = models.DateTimeField('date of release')

    def __str__(self):
        return self.movie_title

    def was_released_recently(self):
        return self.release_date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author_name = models.CharField('author name', max_length=100)
    comment_text = models.CharField('text', max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
