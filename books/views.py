from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Book
from .forms import BookForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView


# Create your views here.

class AddBook(LoginRequiredMixin, CreateView):
    template_name = 'books/add_book.html'
    model = Book
    form_class = BookForm
    success_url = '/books/'

    @method_decorator(permission_required('books.add_book', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        try:
            return super().dispatch(*args, **kwargs)
        except PermissionDenied:
            messages.error(self.request, "You don't have permission to access this page.")
            return HttpResponseRedirect('home')

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(AddBook, self).form_valid(form)



class Books(LoginRequiredMixin, ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = "books/books.html"
    context_object_name = 'books'

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            books = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query) |
                Q(genre__icontains=query) |
                Q(language__icontains=query)
            )
        else:
            books = self.model.objects.all()
        return books



    


class BookDetail(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = 'book'




class EditBook(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'books/edit_book.html'
    model = Book
    form_class = BookForm
    success_url = '/books/'



class DeleteBook(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Book
    success_url = '/books/'

    def test_func(self):
        return self.request.user == self.get_object().user



