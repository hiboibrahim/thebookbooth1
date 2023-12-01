from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'language',
            'genre',
            'status',
            'excerpt'
          
            ]
                  
        labels = {
            'title': 'Book Title',
            'author': 'Author',
            'genre': 'Genre',
            'language': 'Language',
            'status': 'Publish or Draft',
            'excerpt': 'Brief Book Description',
            }


    def save(self, commit=True):
        instance = super(BookForm, self).save(commit=False)


        if commit:
            instance.save()

        return instance
