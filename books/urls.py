from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('books', views.BookView.as_view(), name="books"),
    path('authors', views.AuthorView.as_view(), name="authors"),
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name="book_detail"),
    path('author_detail/<int:pk>', views.AuthorDetailView.as_view(), name="author_detail"),
]