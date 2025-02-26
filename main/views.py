from django.shortcuts import render
from .models import Product, Categories


def home(request):
    hot_products = Product.objects.filter(is_hot_deal=True)
    hot_categories = Categories.objects.filter(is_hot_category=True)

    product_list = Product.objects.all()
    categories = Categories.objects.all()

    popular_categories = Categories.objects.filter(popular_category=True)
    products_popular_category = Product.objects.filter(category__in=hot_categories)

    return render(request, 'home.html', {
        'hot_products': hot_products,
        'product_list': product_list,
        'categories': categories,
        'hot_categories': hot_categories,
        'products_popular_category': products_popular_category,
        'popular_categories': popular_categories,
    })


def category(request):
    return render(request, 'catalog.html')
