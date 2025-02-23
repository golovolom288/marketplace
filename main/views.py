from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    products_list = Product.objects.filter(is_hot_deal=True)
    return render(request, 'home.html', {'products_list': products_list})


def product_detail(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    return render(request, 'news_detail.html', {'news_item': product_item})
