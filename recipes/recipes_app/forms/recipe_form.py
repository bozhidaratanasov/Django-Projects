from django import forms
from recipes_app.models import Recipe

class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = ('title', 'image_url', 'description', 'ingredients', 'time')
