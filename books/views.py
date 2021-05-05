from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Author, Book, Genre


def index(request):
    books = Book.objects.order_by('-rate')[:4]
    context = {
        'books': books
    }
    return render(request, '../templates/index.html', context=context)


class BookView(TemplateView):
    template_name = "templates/books.html"

    def get(self, request, *args, **kwargs):
        num_books = Book.objects.all().count()
        books = Book.objects.all()
        context = {
            'num_books': num_books,
            'books': books
        }
        return render(request, '../templates/books.html', context=context)


class AuthorView(TemplateView):
    template_name = "templates/authors.html"

    def get(self, request, *args, **kwargs):
        num_authors = Author.objects.all().count()
        authors = Author.objects.all()
        context = {
            'num_authors': num_authors,
            'authors': authors
        }

        return render(request, '../templates/authors.html', context=context)


class BookDetailView(TemplateView):
    model = Book
    context_object_name = 'book'
    template_name = '../templates/books_detail.html'

class AuthorDetailView(TemplateView):
    model = Author
    context_object_name = 'author'
    template_name = '../templates/authors_detail.html'
