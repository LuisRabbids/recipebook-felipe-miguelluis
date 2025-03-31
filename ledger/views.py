from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm


@login_required
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


@login_required
def add_recipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            recipe.author = request.user
            recipe.save()
            return redirect("ledger:recipe-detail", id=recipe.id)

    ctx = {"form": form}
    return render(request, "ledger/add_recipe.html", ctx)
