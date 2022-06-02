from django.shortcuts import render

# Create your views here.
from main.models import Product, User, Student, Teacher, Automobile


def advertisemen(request):
    user = User.objects.all()
    student = Student.objects.all()
    teacher = Teacher.objects.all()
    auto = Automobile.objects.all()
    product = Product.objects.all()
    print(request.POST)
    if request.method == 'POST':
        products = Product.objects.filter(title=request.POST.get('products'))
        print(products)
        if products:
            context = {
                'products': products
            }
            return render(request, 'page_index.html', context)
        else:
            context = {
                'error': 'Поиск не дал результата'
            }
            return render(request, 'page_index.html', context)

    context = {
        'product': product,
        'user': user,
        'student': student,
        'teacher': teacher,
        'auto': auto
    }

    return render(request, 'page_index.html', context)