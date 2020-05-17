from django.shortcuts import render
from .models import Drink

# Create your views here.
def drinks_index(request):
    drinks = Drink.objects.all()
    context = {
        'drinks': drinks
    }
    return render(request, 'drinks_index.html', context)


def drink_detail(request, drinkkey):
    drink = Drink.objects.get(pk=drinkkey)
    context = {
        'drink': drink,
    }
    return render(request, 'drink_detail.html', context)


def drink_category(request, category):
    drinks = Drink.objects.filter(
        categories__name__contains=category)
    context = {
        "category": category,
        "drinks": drinks,
    }
    return render(request, 'drink_category.html', context)
