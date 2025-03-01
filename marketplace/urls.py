"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
<<<<<<< Updated upstream

    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('<slug:parent_slug>/<slug:slug>/', views.category_products, name='category_products'),
    path('<slug:slug>/', views.category_products, name='category_products'),

=======
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('catalog/', views.catalog, name='catalog'),
    path('user/', include('user.urls')),
>>>>>>> Stashed changes
]
