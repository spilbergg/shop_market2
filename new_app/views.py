from django.shortcuts import render, redirect

from market_30.utils import validate_name, validate_name_uniq
from .forms import PersonForm
from .models import Person


def index(request):
    form = PersonForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {
                'form': form,
            }
            return render(request, 'page_index.html', context)
    return render(request, 'page_index.html', context)


def new_person_form(request):
    person = Person.objects.all()
    context = {
        'person': person
    }
    if request.method == 'POST':
        a = request.POST
        error_n = ''
        error_l = ''
        error_p = ''
        if validate_name(a['nickname']):
            error_n = 'поле пустое, корректно введите имя'
        if validate_name(a['login']):
            error_l = 'заполните поле'
        if validate_name(a['password']):
            error_p = 'пароль не валидный'
        if validate_name_uniq(a['login']):
            error_l = 'данный логин уже существует'
        if error_n == '' and error_l == '' and error_p == '' and request.FILES['photo'] != None:
            Person.objects.create(nickname=a['nickname'], login=a['login'], password=a['password'], photo=request.FILES['photo'])
            # return redirect('market:main_page')
        else:
            context = {
            'error_n': error_n,
            'error_l': error_l,
            'error_p': error_p,
            'a': a,
        }


    return render(request, 'page_index.html', context)