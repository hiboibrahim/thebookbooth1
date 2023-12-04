from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "image",
            "language",
            "genre",
            "summary",
        ]

        labels = {
            "title": "Book Title",
            "author": "Author",
            "image": "Book Cover",
            "genre": "Genre",
            "language": "Language",
            "summary": "Brief Book Summary",
        }

    def save(self, commit=True):
        instance = super(BookForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance
