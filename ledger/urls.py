from django.urls import path
from .views import recipes_lists, recipe_detail, add_recipe, add_recipe_image

urlpatterns = [
    path('recipes/list', recipes_lists, name="recipes-lists"),
    path("recipe/<int:pk>/", recipe_detail, name="recipe-detail"),
    path("recipe/add/", add_recipe, name="add-recipe"),
    path("recipe/<int:pk>/add_image/", add_recipe_image, name="add-recipe-image"),
]

app_name = 'ledger'
