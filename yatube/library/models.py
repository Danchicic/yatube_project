from django.db import models
from django.db.models import Choices

genre_choices = {'metalic': 'metalic', 'rap': 'rap'}


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    author = models.CharField(max_length=200)
    genre_id = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    pages = models.IntegerField()


class CD(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=40)
    genre = models.CharField(choices=genre_choices, max_length=100)
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=10**5)
    comment = models.TextField(blank=True)

    """Имя (name), текстовая строка, не более 100 символов.
Электронная почта для обратной связи (email)
Название альбома (title), текстовая строка, не более 100 символов.
Исполнитель (artist), текстовая строка, не более 40 символов.
Жанр (genre), поле выбора из предустановленных значений.
Стоимость (price), числовое поле, десятичные числа; необязательное.
Комментарий (comment), многострочное текстовое поле; необязательное.
"""
