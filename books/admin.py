from django.contrib import admin
from .models import Genre, Language, Book

admin.site.register(Genre)
admin.site.register(Language)
@admin.register(Book)


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "genre",
        "language",
       
    )
    list_filter = ('title', 'genre',)
        

