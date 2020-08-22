import uuid

from django.db import models


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    director = models.CharField(max_length=50, blank=True)
    producer = models.CharField(max_length=50, blank=True)
    release_date = models.IntegerField(blank=True)

    def __str__(self):
        return self.title


class Character(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True)
    movie = models.ManyToManyField(Movie, related_name="people")

    def __str__(self):
        return self.name
