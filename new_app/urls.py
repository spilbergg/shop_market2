from django.urls import path

from .views import index, new_person_form

app_name = 'new_app'
urlpatterns = [
    path('index/', index, name='index'),
    path('index3/', new_person_form, name='new_person_form')
]