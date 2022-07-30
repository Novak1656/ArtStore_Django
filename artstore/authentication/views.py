import os

from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.files import File
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from .forms import UserRegisterForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            with open(os.path.join(settings.BASE_DIR, 'authentication/static/authentication/img/avatar.jpg'),
                      'rb') as f:
                image_file = File(f)
                user.avatar.save('avatar.jpg', image_file, True)
            user.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегестрировались!')
            return redirect(reverse('main'))
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'authentication/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)
            login(request, user)
            return redirect(reverse('main'))
    else:
        form = UserLoginForm()
    return render(request, 'authentication/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
