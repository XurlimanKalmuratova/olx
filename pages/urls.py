from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('clothes/', clothes, name='clothes'),
    path('clothes/<pk>/', clothes_detail, name='clothes_detail'),
    path('clothes/<int:pk>/delete', clothes_delete, name = 'clothes_delete'),
    path('clothes/<int:pk>/update', clothes_update, name = 'clothes_update'),
    path('electronics/', electronics, name='electronics'),
    path('electronics/<pk>/', elec_detail, name='elec_detail'),
    path('electronics/<pk>/delete', electronics_delete, name = 'electronics_delete'),
    path('electronics/<pk>/update', electronics_update, name = 'electronics_update'),
    path('furnitures/', furnitures, name='furnitures'),
    path('furnitures/<pk>/', fur_detail, name='fur_detail'),
    path('furnitures/<pk>/delete', furniture_delete, name = 'furniture_delete'),
    path('furnitures/<pk>/update', furniture_update, name = 'furniture_update'),
    path('sport/', sports, name='sports'),
    path('sport/<pk>/', sports_detail, name='sports_detail'),
    path('sport/<pk>/delete', sports_delete, name = 'sports_delete'),
    path('sport/<pk>/update', sports_update, name = 'sports_update'),
    path('household/', households, name='household'),
    path('household/<pk>/', house_detail, name='house_detail'),
    path('household/<pk>/delete', household_delete, name = 'household_delete'),
    path('household/<pk>/update', household_update, name = 'household_update'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('create/', create, name='creates' ),
    path('createclothes/', createclothes, name='createclothes'),
    path('createelectronics/', createelectronics, name='createelectronics'),
    path('createfurnitures/', createfurniture, name='createfurniture'),
    path('createhousehold/', createhousehold, name='createhousehold'),
    path('createsports/', createsports, name='createsports')
]