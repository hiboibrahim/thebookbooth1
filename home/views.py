from django.views.generic import ListView
from books.models import Book


class Index(ListView):
    template_name = 'home/index.html'
    model = Book
    context_object_name = 'books'

    def get_queryset(self):
            return self.model.objects.all()[:3]
