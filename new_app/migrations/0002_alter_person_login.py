# Generated by Django 4.0.4 on 2022-06-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='login',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
