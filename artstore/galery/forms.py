from django import forms
from .models import Art


class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = ['title', 'art', 'genre', 'prise']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'art': forms.FileInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'prise': forms.NumberInput(attrs={'class': 'form-control'})
        }


class UpdateArtForm(forms.ModelForm):
    class Meta:
        model = Art
        fields = ['title', 'genre', 'prise']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'prise': forms.NumberInput(attrs={'class': 'form-control'})
        }
