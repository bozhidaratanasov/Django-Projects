from recipes_app.models import Recipe
from django.shortcuts import redirect, render
from recipes_app.forms.recipe_form import RecipeForm
from recipes_app.forms.recipe_form_readonly import RecipeFormReadonly

def index(request):
    context = {
        'recipes': Recipe.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'GET':
        context = {
            'form': RecipeForm(),
        }

        return render(request, 'create.html', context)
    
    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        context = {
            'form': form
        }

        return render(request, 'create.html', context)

def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': RecipeForm(instance=recipe)
        }

        return render(request, 'edit.html', context)

    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        context = {
            'recipe': recipe,
            'form': form,
        }

        return render(request, 'edit.html', context)

def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': RecipeFormReadonly(instance=recipe),
        }

        return render(request, 'delete.html', context)

    else:
        recipe.delete()
        return redirect('index')

def details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }

    return render(request, 'details.html', context)
