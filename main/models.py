from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    category_img = models.ImageField(upload_to='static/category_images', blank=True, null=True, verbose_name='Изображение Категории')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    is_hot_category = models.BooleanField(default=True, verbose_name="Hot Category!")
    popular_category = models.BooleanField(default=True, verbose_name="Popular Category!")

    class Meta:
        db_table: str = 'category'
        verbose_name: str = 'Категория'
        verbose_name_plural: str = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категория')
    is_hot_deal = models.BooleanField(default=True, verbose_name="Hot Deal!")

    def get_main_image(self):
        first_image = self.images.first()
        return first_image.image.url if first_image else None

    class Meta:
        db_table: str = 'product'
        verbose_name: str = 'Продукт'
        verbose_name_plural: str = 'Продукты'

    def __str__(self):
        return f"{self.name} ({self.category})"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="static/good_images/")
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.product.name}"
