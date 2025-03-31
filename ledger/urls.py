from django.urls import path
from .views import recipes_lists, recipe_detail, add_recipe

urlpatterns = [
    path('recipes/list', recipes_lists, name="recipes-lists"),
    path("recipe/<int:id>/", recipe_detail, name="recipe-detail"),
    path("recipe/add/", add_recipe, name="add-recipe")
]

app_name = 'ledger'
