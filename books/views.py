from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Book
from .forms import BookForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView


# Create your views here.

class AddBook(LoginRequiredMixin, CreateView):
    template_name = 'books/add_book.html'
    model = Book
    form_class = BookForm
    success_url = '/books/'

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(AddBook, self).form_valid(form)



class BookList(LoginRequiredMixin, ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = "books/books.html"
    


class BookDetail(DetailView):
    model = Book
    template_name = "book/books.html"
    context_object_name = 'books'




class EditBook(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'books/edit_book.html'
    model = Book
    form_class = BookForm
    success_url = '/books/'
    
    def test_func(self):
        return self.request.user == self.get_object().user



class DeleteBook(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Book
    success_url = '/books/'

    def test_func(self):
        return self.request.user == self.get_object().user



