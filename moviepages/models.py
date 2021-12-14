from django.db import models
from datetime import datetime

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    actors = models.CharField(max_length=255)
    producers = models.CharField(max_length=100)
    directors = models.CharField(max_length=100, default = None)
    genre = models.CharField(max_length=20, default = None)
    release_date = models.DateField(default=datetime.today, blank=True)
    poster = models.ImageField(upload_to='photos')
    trailer = models.CharField(max_length=255)

    def __str__(self):
        return (self.title)

class Rating(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return (str(self.movie))

