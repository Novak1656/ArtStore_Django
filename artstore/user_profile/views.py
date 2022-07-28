import os

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserInfoForm, AvatarForm, EmailForm, LoginForm
from authentication.models import User


@login_required
def profile(request):
    return render(request, 'user_profile/profile.html')


@login_required
def profile_config(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        if 'info_success' in request.POST:
            form = UserInfoForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
        if 'avatar_success' in request.POST:
            old_avatar_path = user.avatar.path
            form = AvatarForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                os.remove(old_avatar_path)
                form.save()
        if 'email_success' in request.POST:
            form = EmailForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
        if 'login_success' in request.POST:
            form = LoginForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
        if 'password_success' in request.POST:
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
        return redirect(reverse('profile'))
    else:
        forms = {'userinfoform': UserInfoForm(), 'avatarform': AvatarForm(),
                 'emailform': EmailForm(), 'loginform': LoginForm(),
                 'passwordform': PasswordChangeForm(user=request.user)}
    return render(request, 'user_profile/config.html', forms)
