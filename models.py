# movies/models.py

from django.db import models

class Movie(models.Model):
    # These fields will now be required in forms
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)

    # These fields are still optional
    synopsis = models.TextField(blank=True, null=True)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.release_year})"
