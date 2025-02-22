from django.contrib import admin

from main.models import Categories, Product


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ['name',]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'price', 'category']
