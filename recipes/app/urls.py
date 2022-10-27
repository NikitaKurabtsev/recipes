from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_recipes, name='all_recipes')
]