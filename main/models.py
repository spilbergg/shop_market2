from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Название')
    type_product = models.TextField(null=True, blank=True, verbose_name='Тип продукта')
    discription = models.TextField(null=True, blank=True, verbose_name='описание')
    brand = models.CharField(max_length=50, blank=True, verbose_name='Брэнд')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')


class User(models.Model):
    first_name = models.CharField(max_length=30, blank=False, verbose_name='имя')
    last_name = models.CharField(max_length=40, verbose_name='Фамилия')
    sex = models.CharField(max_length=10, verbose_name='пол')
    age = models.IntegerField()
    mail = models.EmailField(max_length=35, verbose_name='Емейл')
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    cart = models.TextField(blank=True)
    telephone = models.CharField(max_length=33)
    foto = models.ImageField(upload_to='images', blank=True)


class Student(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name='имя')
    surname = models.CharField(max_length=40, verbose_name='Фамилия')
    age = models.IntegerField()
    sex = models.CharField(max_length=30, verbose_name='пол')
    university = models.TextField(null=True, blank=True, verbose_name='ВУЗ')
    faculty = models.TextField(null=True, blank=True, verbose_name='факультет')
    form_education = models.TextField(null=True, blank=True, verbose_name='форма обучения')
    scientific_work = models.TextField(null=True, blank=True, verbose_name='научные работы')
    course = models.TextField(null=True, blank=True, verbose_name='курс')


class Teacher(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name='имя')
    surname = models.CharField(max_length=40, verbose_name='Фамилия')
    age = models.IntegerField()
    sex = models.CharField(max_length=30, verbose_name='пол')
    education = models.CharField(max_length=100)
    place_work = models.CharField(max_length=100)
    discipline = models.CharField(max_length=100)
    scientific_work = models.CharField(max_length=100)


class Automobile(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    body_type = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=100)
    transmission_type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    weight = models.IntegerField()
    year = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    mileage = models.IntegerField()



