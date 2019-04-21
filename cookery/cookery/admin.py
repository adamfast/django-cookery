'''Admin setup for our models'''

from django.contrib import admin

from . import models


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Ingredient, IngredientAdmin)


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'quantity', 'unit_of_measure', 'preparation_method')
    list_filter = ('unit_of_measure',)

admin.site.register(models.RecipeIngredient, RecipeIngredientAdmin)


class RecipeIngredientInline(admin.TabularInline):
    model = models.RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'typical_meal', 'difficulty', 'liked', 'slow_cooker_friendly', 'outdoor_cooking_friendly')
    list_filter = ('typical_meal', 'difficulty', 'liked', 'slow_cooker_friendly', 'outdoor_cooking_friendly')
    search_fields = ('name',)
    inlines = (RecipeIngredientInline,)

admin.site.register(models.Recipe, RecipeAdmin)


class RecipeTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(models.RecipeTag, RecipeTagAdmin)


class MealTimeAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.MealTime, MealTimeAdmin)


class MealAdmin(admin.ModelAdmin):
    list_display = ('date', 'meal', 'recipe_plan')
    list_filter = ('meal',)
    date_hierarchy = 'date'
    prepopulated_fields = {
        'name': ('date', 'meal'),
    }

    def recipe_plan(self, instance):
        return ', '.join([r.name for r in instance.recipes.all()])

admin.site.register(models.Meal, MealAdmin)
