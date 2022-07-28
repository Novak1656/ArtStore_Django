from django.urls import path
from .views import *

urlpatterns = [
    path('', profile, name='profile'),
    path('profile_config/', profile_config, name='profile_config'),
]
