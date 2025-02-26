from django.contrib import admin

from main.models import Categories, Product


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_hot_category', 'popular_category')
    list_editable = ('is_hot_category', 'popular_category')
    search_fields = ['name',]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_hot_deal', 'category')
    list_editable = ('is_hot_deal',)
    search_fields = ['name', 'price', 'category']
    list_filter = ('is_hot_deal', 'name')
