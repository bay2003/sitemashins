from django import forms
from django.contrib.auth.models import User
from .models import Tag
from .models import Category
from django import forms
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Create, Page
from django import forms
from .models import Tag  # Импортируйте Tag из models

class MashForm(forms.ModelForm):
    # name_icontains = forms.CharField(widget=forms.TextInput(attrs={''}))
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    text = forms.CharField(label='Description', widget=forms.Textarea())
    page = forms.ModelChoiceField(queryset=Page.objects.all(), label='Страница')

    class Meta:
        model = Create
        exclude = []  # Убираем 'user' из исключенных полей


class ContactForm(forms.Form):
    name = forms.CharField(label='Название')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')

class PostCategoryForm(forms.ModelForm):
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Create
        fields = ['name', 'text', 'tags', 'image', 'rating']  # Включаем все поля, кроме 'user' и 'category'


