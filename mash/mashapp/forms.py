from django import forms
from django.contrib.auth.models import User
from .models import Create
from .models import Tag
from .models import Category
from django import forms
from .models import Create
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Create, Page
from django import forms
from .models import Tag  # Импортируйте Tag из models

class MashForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    text = forms.CharField(label='Description', widget=forms.Textarea())
    page = forms.ModelChoiceField(queryset=Page.objects.all(), label='Страница')

    class Meta:
        model = Create
        exclude = []  # Убираем 'user' из исключенных полей


# @login_required
# def create_post(request):
#     if request.method == 'POST':
#         form = MashForm(request.POST)
#         if form.is_valid():
#             create_instance = form.save(commit=False)
#             create_instance.user = request.user
#             create_instance.save()
#             page = Page.objects.first()
#             post = Post.objects.create(page=page, title=create_instance.name, content=create_instance.text)
#             return redirect('view_post', post_id=post.id)
#     else:
#         form = MashForm()
#     return render(request, 'mashapp/create.html', {'form': form})