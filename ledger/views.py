from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Recipe


def recipes_lists(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, "ledger/recipes_list.html", ctx)


@login_required
def recipe_detail(request, id):
    ctx = {'recipe': Recipe.objects.get(id=id)}
    return render(request, 'ledger/recipe_detail.html', ctx)
