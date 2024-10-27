from django.db import models

from django.db import models
"""
class Movie(models.Model):
    title = models.CharField(max_length=200, default="Unknown Title")
    image_url = models.URLField(max_length=300)
    iframe_url = models.URLField(max_length=500)

    def __str__(self):
        return self.title """


from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100, default="Unknown Director")
    actors = models.TextField(default="Unknown Actors")
    screenwriters = models.TextField(default="Unknown Screenwriters")  # Senaristler
    imdb_score = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    release_year = models.IntegerField(default=2000)
    category = models.CharField(max_length=100, default="Unknown Category")  # Kategori
    description = models.TextField(default="No description available")  # Film açıklaması
    image_url = models.URLField(max_length=300)
    iframe_url = models.URLField(max_length=500)

    def __str__(self):
        return self.title

    