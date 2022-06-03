from django.http import HttpResponse
from django.shortcuts import render, redirect
from market_30.forms import CategoryForm, ProductForm
from market_30.models import Category, Product, Shop
# from market_30.utils import get_shop


def main_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'main_page.html', context)


def category_sort(request, id):
    categories = Category.objects.all()
    products = Product.objects.filter(categories=id)
    context = {
        "products": products, "categories": categories
    }
    return render(request, 'categories_products.html', context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    z = product.shop_set.all()
    products_in_shop = Product.objects.filter(shop__name='ГИППО')
    print(products_in_shop, "все продукты магазина ГИППО")
    shops_for_products = Shop.objects.filter(products__title='Карамельки')
    print(shops_for_products, "Магазины")
    context = {
        'product': product,
        'shops': z,
    }
    return render(request, 'product_detail.html', context)


def less_forms(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    form = CategoryForm()
    context = {
        'categories': categories,
        'products': products,
        'form': form,
    }
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'less_forms.html', context)


def form_category(request):
    print(request.POST, 'category_form')
    if request.method == 'POST':
        # form = CategoryForm(name=request.POST.get('name'), password=request.POST.get('password'))
        form = CategoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            # name = form.cleaned_data.get('name')
            # name.save()
    # return redirect('market:less_forms')
        context = {'form': form}
        return render(request, 'form_error.html', context)

def form_model(request):
    form = ProductForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'model_form.html', context)


def product_form(request):
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
    return redirect('market:less_forms')


def shop_form(request):
    print(request.POST, 'shop_form')
    return redirect('market:less_forms')


''' функция д\з для добавления категории'''
def add_category(request):
    if request.method == 'POST':
        categoria = request.POST.get('category_name')
        if categoria:
            Category.objects.create(name=categoria)
            return redirect('market:main_page')
    return render(request, 'add_category.html')


# def delete_category(request, id):
#     del_category = Category.objects.get(id=id)
#     del_category.delete()
#     return render(request, 'add_category.html')


''' функция д\з для добавления продукта'''
def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('product_title')
        description = request.POST.get('product_description')
        price = request.POST.get('product_price')
        image = request.FILES.get('product_image')
        created = request.POST.get('product_created')
        update = request.POST.get('product_update')
        product_categories = request.POST.get('product_categories')
        categories = Category.objects.get(name=product_categories)
        shop = request.POST.getlist('product_shop')
        if title and description and price:
            product = Product.objects.create(
                title=title, description=description, price=price,
                image=image, created=created, update=update, categories_id=categories.id
            )

            if shop and product:
                for i in shop:
                    product.shop_set.add(Shop.objects.get(name=i))

        return redirect('market:main_page')

    categori = Category.objects.all()
    product_shops = Shop.objects.all()
    context = {
        'categori': categori,
        'product_shops': product_shops,
    }
    return render(request, 'add_product.html', context)


''' функция д\з для добавления магазина'''
def add_shop(request):
    prod = Product.objects.all()
    if request.method == 'POST':
        shop = request.POST.get('shop_add')
        product = request.POST.getlist('cat_deteil')
        print(product)
        print(shop)
        if shop:
            shop_add = Shop.objects.create(name=shop)
            for i in product:
                shop_add.products.add(Product.objects.get(title=i))
        return redirect('market:main_page')
    context = {
        'prod': prod,
    }
    return render(request, 'add_shop.html', context)

