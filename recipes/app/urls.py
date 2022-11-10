from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.all_recipes, name='recipes'),
    path('recipes/<int:pk>/', views.detail_recipe, name='detail_recipe'),
    path('/recipes/difficult/<str:difficult>/', views.recipe_difficult_detail, name='difficult'),
]
