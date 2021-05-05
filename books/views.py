from django.shortcuts import render
from .models import Author, Book, Genre

def index(request):

    books = Book.objects.order_by('-rate')[:4]
    context = {
        'books': books
    }

    return render(request, '../templates/index.html', context=context)

def book(request):

    num_books = Book.objects.all().count()
    books = Book.objects.all()
    context = {
        'num_books': num_books,
        'books': books
    }

    return render(request, '../templates/books.html', context=context)

def author(request):

    num_authors = Author.objects.all().count()
    authors = Author.objects.all()
    context = {
        'num_authors': num_authors,
        'authors': authors
    }

    return render(request, '../templates/authors.html', context=context)


