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


# Create your views here.

# class AddBook(LoginRequiredMixin, CreateView):
#     template_name = 'books/add_book.html'
#     model = Book
#     form_class = BookForm
#     success_url = '/books/'

#     @method_decorator(permission_required('books.add_book', raise_exception=True))
#     def dispatch(self, *args, **kwargs):
#         try:
#             return super().dispatch(*args, **kwargs)
#         except Exception:
#             messages.error(self.request, "You don't have permission to access this page.")
#             return redirect('home:home')

#     def form_valid(self, form):
#         form.instance.user = self.request.user

#         return super(AddBook, self).form_valid(form)


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




# class EditBook(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     template_name = 'books/edit_book.html'
#     model = Book
#     form_class = BookForm
#     success_url = '/books/'


@login_required
def edit_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    existing_img = book.image
    print(existing_img)
    if book.user != request.user:
        messages.error(request, 'Access denied. Please try again.')
        return redirect('books')
    # user matches the book user / proceed
    if request.method == 'POST':
        form = BookForm(request.POST or None, request.FILES)
        print(request.POST.get("image"))
        if form.is_valid():
            form.instance.image = request.POST.get("image")
            form.save()
            messages.success(request, 'Book successfully updated!')
            return redirect('books')
        messages.error(request, 'An error occurred. Please try again.')
        print(form.errors)
    form = BookForm(instance=book)
    template = 'books/edit_book.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


#class DeleteBook(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
#    model = Book
#    success_url = '/books/'
#
#    def test_func(self):
#        return self.request.user == self.get_object().user

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    if book.user != request.user:
        messages.error(request, 'Access denied. Please try again.')
        return redirect('books')
    # user matches the book user / proceed
    book.delete()
    messages.success(request, 'Book successfully deleted.')
    return redirect('books')