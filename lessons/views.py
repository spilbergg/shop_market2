from django.shortcuts import render
from lessons.models import Droid


def get_droid(request):
    droids = Droid.objects.all()
    print(request.POST)
    if request.method == 'POST':
        droid = Droid.objects.filter(name=request.POST.get('droid'))
        print(droid)
        if droid:
            context = {
                'droid': droid,
            }
            return render(request, 'droids.html', context)

        else:
            context = {
                'error': 'Поиск не дал результата'
            }
            return render(request, 'droids.html', context)

    context = {
        'droids': droids
    }
    return render(request, 'droids.html', context)