from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('templates/books', views.book, name="books"),
    path('templates/authors', views.author, name="authors"),
]