from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField('year published')
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    def __str__(self):
        return f"{self.title} ({self.pub_date.year})"