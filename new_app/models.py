from django.db import models

class Person(models.Model):
    nickname = models.CharField(max_length=20)
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.nickname
