from django import forms

from app.models import Recipe


class RecipeForm(forms.ModelForm):
    
    class meta:
        model = Recipe
        fields = ('__all__',)
