from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField


class Genre(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="books/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    isbn_number = models.CharField(max_length=13, null=True, blank=True)
    genre = models.ForeignKey(Genre, null=False, blank=False, on_delete=models.CASCADE)
    language = models.ForeignKey(
        Language, null=False, blank=False, on_delete=models.CASCADE
    )
    summary = models.TextField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.title
