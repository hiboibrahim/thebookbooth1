from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Book
from .forms import BookForm


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Book successfully added!')
            return redirect('books')
        messages.error(request, 'An error occurred. Please try again.')
    form = BookForm()
    template = 'books/add_book.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


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


@login_required
def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if book.user != request.user:
        messages.error(request, 'Access denied. Please try again.')
        return redirect('books')
    # user matches the book user / proceed
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Book successfully updated!')
            return redirect('books')
        messages.error(request, 'An error occurred. Please try again.')
    form = BookForm(instance=book)
    template = 'books/edit_book.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if book.user != request.user:
        messages.error(request, 'Access denied. Please try again.')
        return redirect('books')
    # user matches the book user / proceed
    book.delete()
    messages.success(request, 'Book successfully deleted.')
    return redirect('books')
