from django.shortcuts import render
from .models import Drink

# Create your views here.
def drinks_index(request):
    context = {
        
    }
    return render(request, 'drink_index.html', context)


def drink_detail(request, pk):
    context = {}
    return render(request, 'drinks_detail.html', context)


def drink_category(request, category):
    context = {}
    return render(request, 'drink_category.html', context)