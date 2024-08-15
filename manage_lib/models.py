from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    number_of_books = models.PositiveIntegerField()


class Books(models.Model):
    title = models.CharField(max_length=200)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_book')
    author = models.CharField(max_length=200)
    published_date = models.DateTimeField()
    isbn = models.CharField(max_length=13)
