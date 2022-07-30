from django.urls import path
from .views import *

urlpatterns = [
    path('', Shop.as_view(), name='main'),
    path('add_in_basket/<int:pk>', add_in_basket, name='add_in_basket'),
    path('basket/', BasketView.as_view(), name='basket'),
    path('delete_basket_art/<int:pk>', delete_basket_art, name='delete_basket_art'),
    path('buy_arts/', buy_arts, name='buy_arts'),
]
