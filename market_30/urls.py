from django.urls import path
from .views import main_page, category_sort, product_detail, product_form, form_category, \
    less_forms, add_product, add_category, add_shop, shop_form, form_model


app_name = 'market'
urlpatterns = [
    path('', main_page, name='main_page'),
    path('<int:id>/', category_sort, name="category_sort"),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('less_forms/', less_forms, name='less_forms'),
    path('add_product/', add_product, name='add_product'),
    path('add_category/', add_category, name='add_category'),
    path('add_shop/', add_shop, name='add_shop'),
    path('category_form/', shop_form, name='shop_form'),
    path('product_form/', product_form, name='product_form'),
    path('form_category/', form_category, name='form_category'),
    path('form_model/', form_model, name='form_model'),

]