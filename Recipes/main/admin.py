from django.contrib import admin

from .models import Recipe, Category, RecipeCategory, Ingredient


# Inline для промежуточной модели RecipeCategory
class RecipeCategoryInline(admin.TabularInline):
    model = RecipeCategory
    extra = 1  # Сколько строк будет изначально в форме

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'cooking_time', 'image')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'steps', 'cooking_time', 'image', 'author', 'ingredients')
        }),
    )
    inlines = [RecipeCategoryInline]  # Включаем RecipeCategory как inline

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
admin.site.register(RecipeCategory)
admin.site.register(Ingredient)
