from django.shortcuts import render
from .models import Author, Book, Genre

def index(request):

    num_books = Book.objects.all().count()
    books = Book.objects.order_by('-rate')[:6]
    context = {
        'num_books': num_books,
        'books': books
    }

    return render(request, '../templates/index.html', context=context)


