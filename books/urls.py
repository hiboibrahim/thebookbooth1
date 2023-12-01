from django.urls import path
from .views import AddBook, BookList


urlpatterns = [
    path('', AddBook.as_view(), name='add_book'),
    path('', BookList.as_view(), name='books'),

]


