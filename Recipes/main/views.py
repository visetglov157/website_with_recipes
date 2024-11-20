from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RecipeForm
from .models import Recipe


def index(request):
    latest_recipes = Recipe.objects.all().order_by('-id')[:5]
    return render(request, 'index.html', {'recipes': latest_recipes})

def about(request):
    return render(request, 'about.html')

def recipe_list(request):
    query = request.GET.get('title')
    recipes = Recipe.objects.all().order_by('title')

    if query:  # Если пользователь ввел запрос
        query = query.lower()  # Приводим запрос к нижнему регистру
        recipes = [recipe for recipe in recipes if query in recipe.title.lower()]

    return render(request, 'recipe_list.html', {'recipes': recipes, 'query': query,
                                                'title': 'Все рецепты'})

def recipe_user(request):
    query = request.GET.get('title')
    recipes = Recipe.objects.filter(author=request.user).order_by('title')

    if query:  # Если пользователь ввел запрос
        query = query.lower()  # Приводим запрос к нижнему регистру
        recipes = [recipe for recipe in recipes if query in recipe.title.lower()]

    return render(request, 'recipe_list.html', {'recipes': recipes, 'query': query,
                                                'title': 'Мои рецепты'})

def recipe_detail(request, recipe_id):
    # Извлекаем рецепт по первичному ключу (id)
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    # Передаем рецепт в шаблон
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # Установить текущего пользователя автором
            recipe.save()
            form.save_m2m()  # Сохранить связи ManyToMany
            return redirect('recipe_user')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form, 'title': "Добавить рецепт"})

@login_required
def recipe_edit(request, recipe_id):
    # Извлекаем рецепт по первичному ключу (pk)
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('recipe_user')
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipe_form.html', {'form': form, 'title': "Редактировать рецепт"})

@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_user')
    return render(request, 'recipe_confirm_delete.html', {'recipe': recipe})