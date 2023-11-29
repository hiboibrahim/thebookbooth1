# from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from books.models import Book


# Create your views here.
# class Index(TemplateView):
    # template_name = 'home/index.html'

class BookList(ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = "home/index.html"