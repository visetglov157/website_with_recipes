from django import forms
from .models import Recipe, Category, Ingredient
from .widgets import CustomCheckboxSelectMultiple


class RecipeForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all().order_by('name'),
        widget=CustomCheckboxSelectMultiple(attrs={
            'id': 'categories'
        }),
        required=True,
        label="Категории"
    )
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all().order_by('name'),
        widget=CustomCheckboxSelectMultiple(attrs={
            'id': 'ingredients'
        }),
        required=True,
        label="Ингредиенты"
    )

    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'steps',
            'cooking_time',
            'image',
            'categories',
            'ingredients'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Описание рецепта'}),
            'steps': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Шаги приготовления'}),
            'cooking_time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Время в минутах'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'steps': 'Шаги приготовления',
            'cooking_time': 'Время приготовления (минуты)',
            'image': 'Изображение',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Кастомизация полей для единообразия
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs['class'] = 'form-control'