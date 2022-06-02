from django.db import models


class Droid(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    master = models.CharField(max_length=100, verbose_name='Хозяин')
    planet = models.CharField(max_length=50, verbose_name='Планета')
    image = models.ImageField(upload_to='images', blank=True, verbose_name='Изображение')