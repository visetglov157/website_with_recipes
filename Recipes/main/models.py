from django.db import models
from django.contrib.auth.models import User


# Категории рецептов
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")  # Необязательное поле

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# Ингредиенты
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


# Рецепты
class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    steps = models.TextField(verbose_name="Шаги приготовления")  # Хранится как текст
    cooking_time = models.PositiveIntegerField(verbose_name="Время приготовления (минуты)")
    image = models.ImageField(upload_to='recipes/images/', blank=True, null=True, verbose_name="Изображение")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    ingredients = models.ManyToManyField(Ingredient, verbose_name="Ингредиенты", blank=True)
    categories = models.ManyToManyField(Category, through='RecipeCategory', verbose_name="Категории")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


# Связующая таблица для рецептов и категорий
class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")  # Обязательное поле

    class Meta:
        verbose_name = "Категория рецепта"
        verbose_name_plural = "Категории рецептов"
        unique_together = ('recipe', 'category')  # Чтобы не было повторов

    def __str__(self):
        return f"{self.recipe.title} -> {self.category.name}"
