from django.forms.widgets import SelectMultiple
from django.utils.safestring import mark_safe

class CustomCheckboxSelectMultiple(SelectMultiple):
    def render(self, name, value, attrs=None, choices=(), renderer=None):
        # Добавляем 'name' в attrs, если его нет
        if attrs is None:
            attrs = {}
        attrs['name'] = name

        # Генерация уникального id, если оно не задано
        if 'id' not in attrs:
            attrs['id'] = f'{name}_id'

        output = ['<div class="checkbox-container">']  # Начинаем общий контейнер для всех чекбоксов
        str_values = set(map(str, value or []))

        for i, (option_value, option_label) in enumerate(self.choices):
            # Генерируем уникальный id для каждого чекбокса
            checkbox_id = f'{attrs["id"]}_{i}'
            is_checked = 'checked' if str(option_value) in str_values else ''
            checkbox = f'<input type="checkbox" name="{name}" value="{option_value}" id="{checkbox_id}" {is_checked}>'
            label = f'<label for="{checkbox_id}">{checkbox}<span class="checkmark"></span>{option_label}</label>'
            output.append(f'<div class="custom-checkbox">{label}</div>')  # Каждый чекбокс в отдельный div

        output.append('</div>')  # Закрываем контейнер

        return mark_safe('\n'.join(output))
