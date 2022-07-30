import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ArtForm, UpdateArtForm


@login_required
def gallery(request):
    arts = request.user.gallery.all()
    return render(request, 'gallery/gallery.html', {'arts': arts})


@login_required
def add_art(request):
    if request.user.roles != 'Автор':
        return redirect(reverse('main'))
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            art = form.save(commit=False)
            art.author = request.user
            form.save()
            return redirect(reverse('gallery'))
    else:
        form = ArtForm()
    return render(request, 'gallery/add_art.html', {'form': form})


@login_required
def update_art(request, pk):
    if request.user.roles != 'Автор':
        return redirect(reverse('main'))
    art = request.user.art.get(pk=pk)
    if request.method == 'POST':
        form = UpdateArtForm(request.POST, instance=art)
        if form.is_valid():
            form.save()
            return redirect(reverse('gallery'))
    else:
        form = UpdateArtForm(art)
    return render(request, 'gallery/update_art.html', {'form': form})


@login_required
def delete_art(request, pk, is_gallery=0):
    if request.user.roles != 'Автор':
        return redirect(reverse('main'))
    if is_gallery == 1:
        art = request.user.gallery.get(pk=pk)
    else:
        art = request.user.art.get(pk=pk)
    os.remove(art.art.path)
    art.delete()
    return redirect(reverse('gallery'))
