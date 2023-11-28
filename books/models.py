from django.db import models

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=13)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    published_date = models.DateTimeField()

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name

      