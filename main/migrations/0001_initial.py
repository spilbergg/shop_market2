# Generated by Django 4.0.4 on 2022-04-23 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('body_type', models.CharField(max_length=100)),
                ('engine_type', models.CharField(max_length=100)),
                ('transmission_type', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('mileage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='Название')),
                ('type_product', models.TextField(blank=True, null=True, verbose_name='Тип продукта')),
                ('discription', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('brand', models.CharField(blank=True, max_length=50, verbose_name='Брэнд')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='имя')),
                ('surname', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=30, verbose_name='пол')),
                ('university', models.TextField(blank=True, null=True, verbose_name='ВУЗ')),
                ('faculty', models.TextField(blank=True, null=True, verbose_name='факультет')),
                ('form_education', models.TextField(blank=True, null=True, verbose_name='форма обучения')),
                ('scientific_work', models.TextField(blank=True, null=True, verbose_name='научные работы')),
                ('course', models.TextField(blank=True, null=True, verbose_name='курс')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='имя')),
                ('surname', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=30, verbose_name='пол')),
                ('education', models.CharField(max_length=100)),
                ('place_work', models.CharField(max_length=100)),
                ('discipline', models.CharField(max_length=100)),
                ('scientific_work', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='имя')),
                ('last_name', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('sex', models.CharField(max_length=10, verbose_name='пол')),
                ('age', models.IntegerField()),
                ('mail', models.EmailField(max_length=35, verbose_name='Емейл')),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('cart', models.TextField(null=True)),
                ('telephone', models.CharField(max_length=33)),
                ('foto', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
