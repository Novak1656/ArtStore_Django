from django.urls import path
from .views import *

urlpatterns = [
    path('', gallery, name='gallery'),
    path('add_art/', add_art, name='add_art'),
    path('update_art/<int:pk>', update_art, name='update_art'),
    path('delete_art/<int:pk>/<int:is_gallery>', delete_art, name='delete_art'),
]
