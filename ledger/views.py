from django.shortcuts import render
from .models import Recipe


def recipes_lists(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, "ledger/recipes_list.html", ctx)


def recipe_detail(request, id):
    ctx = {'recipe': Recipe.objects.get(id=id)}
    return render(request, 'ledger/recipe_detail.html', ctx)
