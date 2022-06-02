from django.contrib import admin
from main.models import Student
from main.models import User
from main.models import Product
from main.models import Teacher
from main.models import Automobile

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Automobile)

