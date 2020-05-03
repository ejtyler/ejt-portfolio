from django.urls import path
from . import views

STATIC_URL = '/static/'

urlpatterns = [
    path("", views.home, name='pages_index'),
]