from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm, RecipeImageForm


@login_required
def recipes_lists(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes': recipes
    }
    return render(request, "ledger/recipes_list.html", ctx)


@login_required
def recipe_detail(request, pk):
    ctx = {'recipe': Recipe.objects.get(pk=pk)}
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
            return redirect("ledger:recipe-detail", pk=recipe.pk)

    ctx = {"form": form}
    return render(request, "ledger/add_recipe.html", ctx)


@login_required
def add_recipe_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeImageForm()

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.recipe = recipe  
            image.save()
            return redirect("ledger:recipe-detail", pk=recipe.pk)
        
    ctx = {"form": form, "recipe": recipe}
    return render(request, "ledger/add_recipe_image.html", ctx)