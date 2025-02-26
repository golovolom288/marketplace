from django.contrib import admin
from main.models import Category, Product, ProductImage


class SubCategoryInline(admin.TabularInline):  # Встроенные подкатегории
    model = Category
    fk_name = "parent_category"
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'is_hot_category', 'popular_category')
    list_editable = ('is_hot_category', 'popular_category')
    search_fields = ['name']
    list_filter = ('parent_category', 'is_hot_category', 'popular_category')
    inlines = [SubCategoryInline]  # Вложенные подкатегории внутри категории


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Количество пустых полей для добавления новых фото


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_hot_deal', 'category')
    list_editable = ('is_hot_deal',)
    search_fields = ['name', 'price', 'category']
    list_filter = ('is_hot_deal', 'name')
    inlines = [ProductImageInline]


admin.site.register(ProductImage)
