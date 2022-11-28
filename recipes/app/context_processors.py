from app.models import Recipe, Difficult


def recipe_context(request):
    recipes = Recipe.objects.all()

    return {'recipes': recipes}


def recipe_difficult(request):
    recipe_difficult = Difficult.objects.all()
    
    return {'recipe_difficult': recipe_difficult}