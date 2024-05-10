from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField()