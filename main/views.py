from django.http import JsonResponse
from django.shortcuts import render
# from .models import Quest


def home(request):
    return render(request, 'home.html')
