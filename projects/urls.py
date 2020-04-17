from django.urls import path
from . import views

STATIC_URL = '/static/'

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:projectkey>/", views.project_detail, name="project_detail"),
]
