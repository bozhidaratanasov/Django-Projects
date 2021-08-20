from recipes_app.models import Recipe
from django.urls import path
from recipes_app.views import create, index, edit, delete, details

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create recipe'),
    path('edit/<int:pk>', edit, name='edit recipe'),
    path('delete/<int:pk>', delete, name='delete recipe'),
    path('details/<int:pk>', details, name='recipe details'),
]
