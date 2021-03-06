# Generated by Django 3.2.1 on 2021-05-04 17:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter author's name", max_length=100, unique=True, verbose_name='Genre name')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Biography')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter a book genre', max_length=50, unique=True, verbose_name='Genre name'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('plot', models.TextField(blank=True, null=True, verbose_name='Plot')),
                ('rate', models.IntegerField(default=0, help_text='Please enter integer value (range 0 - 5)', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Rate')),
                ('author', models.ManyToManyField(help_text='Select author of this book', to='books.Author')),
                ('genres', models.ManyToManyField(help_text='Select genre of this book', to='books.Genre')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
