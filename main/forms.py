from django import forms
from .models import Category


class ProductFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), required=False, empty_label="Все категории", label="Категория"
    )
    min_price = forms.DecimalField(required=False, min_value=0, label="Мин. цена")
    max_price = forms.DecimalField(required=False, min_value=0, label="Макс. цена")
    sort_by = forms.ChoiceField(
        choices=[
            ("name", "Название"),
            ("price_asc", "Цена (по возрастанию)"),
            ("price_desc", "Цена (по убыванию)"),
        ],
        required=False,
        label="Сортировать по",
    )
