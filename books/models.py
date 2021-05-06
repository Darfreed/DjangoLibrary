from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

def cover_path(instance, filename):
    return "book/covers/" + str(instance.id) + "/" + filename

def portrait_path(instance, filename):
    return "book/portraits/" + str(instance.id) + "/" + filename

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Genre name",
                            help_text='Enter a book genre')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Author's name",
                            help_text='Enter author\'s name')
    bio = models.TextField(blank=True, null=True, verbose_name="Biography")
    portrait = models.ImageField(upload_to=portrait_path, blank=True, null=True, verbose_name="Portrait")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    author = models.ManyToManyField(Author, help_text='Select author of this book')

    TYPE_OF_BOOK = (
        ('epika', 'Epika'),
        ('lyrika', 'Lyrika'),
        ('drama', 'Drama'),
    )

    type = models.CharField(max_length=6, choices=TYPE_OF_BOOK, default='image')
    genres = models.ManyToManyField(Genre, help_text='Select genre of this book')
    plot = models.TextField(blank=True, null=True, verbose_name="Plot")
    rate = models.FloatField(default=0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], null=True,
                               help_text="Please enter float value (range 0.0 - 5.0)", verbose_name="Rate")
    cover = models.ImageField(upload_to=cover_path, blank=True, null=True, verbose_name="Cover")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])




