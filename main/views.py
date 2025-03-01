from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    hot_products = Product.objects.filter(is_hot_deal=True)
    hot_categories = Category.objects.filter(is_hot_category=True)

    product_list = Product.objects.all()
    categories = Category.objects.filter(parent_category__isnull=True).prefetch_related("subcategories")

    popular_categories = Category.objects.filter(popular_category=True)
    products_popular_category = Product.objects.filter(category__in=hot_categories)

    return render(request, 'home.html', {
        'hot_products': hot_products,
        'product_list': product_list,
        'categories': categories,
        'hot_categories': hot_categories,
        'products_popular_category': products_popular_category,
        'popular_categories': popular_categories,
    })


def get_category_path(category):
    path = []
    while category:
        path.append(category)
        category = category.parent_category
    return list(reversed(path))


def product_detail(request, slug, parent_slug=None):
    product_item = get_object_or_404(Product, slug=slug)
    product_images = product_item.images.all()
    category = product_item.category

    category_path = get_category_path(category)
    parent_slug = category.parent_category.slug if category.parent_category else None

    return render(request, 'product_detail.html', {
        'product_item': product_item,
        'product_images': product_images,
        'category': category,
        'category_path': category_path,
        'parent_slug': parent_slug,
    })


def category_products(request, slug, parent_slug=None):
    category = get_category_path_from_slug(slug, parent_slug)

    subcategories = category.subcategories.all()
    products = Product.objects.filter(category__in=[category] + list(subcategories)) if subcategories.exists() else Product.objects.filter(category=category)

    return render(request, 'category_products.html', {'category': category, 'products': products})


def get_category_path_from_slug(slug, parent_slug=None):  # Тут я получаю категорию и её подкатегории по слагу.
    if parent_slug:
        parent_category = get_object_or_404(Category, slug=parent_slug)
        category = get_object_or_404(Category, slug=slug, parent_category=parent_category)
    else:
        category = get_object_or_404(Category, slug=slug, parent_category__isnull=True)

    return category


def blog(request):
    return render(request, 'blog.html')


def contacts(request):
    return render(request, 'contacts.html')
