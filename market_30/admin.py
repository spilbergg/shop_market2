from django.contrib import admin

# Register your models here.
from market_30.models import Category, Product

from market_30.models import Shop

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Shop)