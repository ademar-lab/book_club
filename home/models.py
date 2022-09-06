from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    release_year = models.SmallIntegerField()
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Chapter(models.Model):
    subtitle = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subtitle}'