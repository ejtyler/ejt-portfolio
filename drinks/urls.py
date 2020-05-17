from django.urls import path
from . import views


urlpatterns = [
    path("", views.drinks_index, name='drinks_index'),
    path("<int:drinkkey>/", views.drink_detail, name='drink_detail'),
    path("<category>/", views.drink_category, name='drink_category'),
]
