from django.urls import path
from .views import recipes_lists, recipe_detail

urlpatterns = [
    path('recipes/list', recipes_lists, name="recipes-lists"),
    path("recipe/<int:id>/", recipe_detail, name="recipe_detail"),
]

app_name = 'ledger'
