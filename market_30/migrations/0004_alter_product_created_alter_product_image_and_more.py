# Generated by Django 4.0.4 on 2022-05-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_30', '0003_rename_descriplion_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='city',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='street',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
