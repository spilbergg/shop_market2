# Generated by Django 4.0.4 on 2022-04-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cart',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
