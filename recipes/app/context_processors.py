from app.models import Recipe


def recipe_context(request):
    recipes = Recipe.objects.all()
    return {'recipes': recipes}