from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='',
                                widget=forms.TextInput(attrs={"class": "form-control form-control-lg bg-transparent mr-2",
                                                              "placeholder": "Логин",
                                                              "aria-label": "Username"}))
    email = forms.CharField(max_length=255, label='',
                            widget=forms.EmailInput(attrs={"class": "form-control form-control-lg bg-transparent mr-2",
                                                           "placeholder": "Электронная почта",
                                                           "aria-label": "Email"}))
    password1 = forms.CharField(max_length=255, label='',
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control form-control-lg bg-transparent mr-2",
                                           "placeholder": "Пароль", "aria-label": "Password1"}))
    password2 = forms.CharField(max_length=255, label='',
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control form-control-lg bg-transparent mr-2",
                                           "placeholder": "Повторите пароль", "aria-label": "Password2"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='',
                                widget=forms.TextInput(attrs={"class": "form-control form-control-lg bg-transparent mr-2",
                                                              "placeholder": "Логин",
                                                              "aria-label": "Username"}))
    password = forms.CharField(max_length=255, label='',
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-control form-control-lg bg-transparent mr-2",
                                          "placeholder": "Пароль", "aria-label": "Пароль"}))

class BootstrapErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return mark_safe('<ul class="m-0">%s</ul>' % ''.join(['<li class="text-danger">%s</li>' % e for e in self]))