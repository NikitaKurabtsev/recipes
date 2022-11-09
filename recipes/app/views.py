from django.http import HttpResponse
from django.shortcuts import render

from app.models import Recipe


# Create your views here.
def all_recipes(request):
    recipes = Recipe.objects.all()
    recipes_count = Recipe.objects.count()
    context = {
        'recipes': recipes,
        'recipes_count': recipes_count
    }
    return render(request, 'app/recipes.html', context)
