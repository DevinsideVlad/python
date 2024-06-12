from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from products.models import ProductCategory, Product, Basket, ProductFilter
from products.forms import QuantityForm
from users.models import User
from products.models import Product
from django.core.paginator import Paginator


def index(request):
    context = {'title': 'Салон проката', }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, filter_id=None, page_number=1):
    if category_id:
        category = ProductCategory.objects.get(id=category_id)
        products = Product.objects.filter(category=category)

    elif filter_id:
        if filter_id == 1:
            products = Product.objects.all().order_by('price')
        elif filter_id == 2:
            products = Product.objects.all().order_by('-price')
        elif filter_id == 3:
            products = Product.objects.all().order_by('name')
        elif filter_id == 4:
            products = Product.objects.filter(price__lt=600)

    else:
        products = Product.objects.all()

    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Прокат - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
        'filters': ProductFilter.objects.all(),
    }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        # basket.quantity += 1
        basket.save()

        return redirect('orders:order-create')

        # return HttpResponseRedirect(request.META['HTTP_REFERER'])
        # return render(request, 'orders/order-create.html')


def product_page(request, product_id):
    product = Product.objects.get(id=product_id)
    dele = Basket.objects.get(user=request.user)
    dele.delete()
    basket, created = Basket.objects.get_or_create(user=request.user, product=product)
    if request.method == 'POST':
        form = QuantityForm(instance=basket, data=request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('products:product_page'))
    else:
        form = QuantityForm()
    return render(request, 'products/product_page.html', {'product': product, 'form': form})


# def quantity_input(request, product_id):
#     product = Product.objects.get(id=product_id)
#     basket = Basket.objects.get(user=request.user, product=product)
#     if request.method == 'POST':
#         form = QuantityForm(instance=basket, data=request.POST)
#         if form.is_valid():
#             form.save()
#
#     else:
#         form = QuantityForm(instance=basket)
#     context = {'form': form}
#     return render(request, context)


def about(request):
    return render(request, 'products/about.html')
