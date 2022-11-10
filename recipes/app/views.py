from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from app.models import Recipe


def all_recipes(request):
    recipes = request.GET
    if recipes:
        q = recipes.get('search')
        recipes = Recipe.objects.filter(name__icontains=q)

        return render(request, 'app/recipes.html', {'recipes': recipes})

    recipes = Recipe.objects.all()

    return render(request, 'app/recipes.html', {'recipes': recipes})


def detail_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    context = {
        'recipe': recipe
    }

    return render(request, 'app/recipe_detail.html', context)
