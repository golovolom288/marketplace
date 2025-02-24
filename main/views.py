from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Product, Categories


def home(request):
    hot_products = Product.objects.filter(is_hot_deal=True)
    hot_categories = Categories.objects.filter(is_hot_category=True)

    product_list = Product.objects.all()
    categories = Categories.objects.all()
    return render(request, 'home.html', {
        'hot_products': hot_products,
        'product_list': product_list,
        'categories': categories,
        'hot_categories': hot_categories,
    })


def category(request):
    return render(request, 'catalog.html')
