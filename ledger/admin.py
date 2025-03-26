from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
#start