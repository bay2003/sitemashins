from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import RegistrationForm
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import BlogUser
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'


class UserCreateView(CreateView):
    model =BlogUser
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy ('users:login')

def logout_view(request):
    logout(request)
    # После выхода пользователя перенаправляем на страницу, где он может войти заново или на другую страницу, например, на главную.
    return redirect('index')  # Здесь 'home' - это имя URL-шаблона, на который вы хотите перенаправить пользователя после выхода.


# Create your views here.



