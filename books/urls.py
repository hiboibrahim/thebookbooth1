from . import views
from django.urls import path
from .views import Books, BookDetail


urlpatterns = [
    # path("add_book/", AddBook.as_view(), name="add_book"),
    path("add_book/", views.add_book, name="add_book"),
    path("books/", views.Books.as_view(), name="books"),
    path("<slug:pk>/", views.BookDetail.as_view(), name="book_detail"),
    path("delete/<slug:pk>/", views.delete_book, name="delete_book"),
    path("edit/<int:pk>/", views.edit_book, name="edit_book"),
]
