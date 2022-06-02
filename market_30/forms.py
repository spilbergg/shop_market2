from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Model
from django.forms import ModelForm
from market_30.models import Category, Product

def valid_name(name):
    if name == 'Johan':
        print(name)
    else:
        raise ValidationError('Имя не Johan')
class CategoryForm(forms.Form):
    name = forms.CharField(label='Категория', max_length=100, validators=[valid_name])
    password = forms.CharField(widget=forms.PasswordInput)
    price = forms.DecimalField(max_digits=8, decimal_places=2)

    def save(self):
        return Category.objects.create(name=self.cleaned_data['name'])




class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image', 'categories']


class ShopForm(forms.Form):
    pass