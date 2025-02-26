from django.shortcuts import render, get_object_or_404
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


def product_detail(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    product_images = product_item.images.all()  # Загружаем все изображения товара

    return render(request, 'product_detail.html', {
        'product_item': product_item,
        'product_images': product_images
    })


def catalog(request):
    return render(request, 'catalog.html')
