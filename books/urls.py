from . import views
from django.urls import path
from .views import AddBook, BookList, BookDetail, DeleteBook, EditBook


urlpatterns = [
    path('', AddBook.as_view(), name='add_book'),
    path('books/', views.BookList.as_view(), name='books'),
    path("<slug:pk>/", views.BookDetail.as_view(), name="book_detail"),
    path("delete/<slug:pk>/", views.DeleteBook.as_view(), name="delete_book"),
    path("edit/<slug:pk>/", EditBook.as_view(), name="edit_book"),


]


