from django.urls import path
from . import views


urlpatterns = [
    path("", views.drinks_index, name='drinks_index'),
    path("<int:pk>/", views.drink_detail, name='drink_detail'),
    path("<category>/", views.drink_category, name='drink_category'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
]