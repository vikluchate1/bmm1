from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите Username"
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите E-mail"
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите пароль"
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Подтвердите пароль"
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите Username"
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите пароль"
    }))

    class Meta:
        model = User
        fields = ('username', 'password')
