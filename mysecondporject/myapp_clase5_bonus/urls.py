
from os import name
from django.urls import path
from . import views

urlpatterns = [
   path('Comprar/', views.Comprar, name='Comprar'),
   path('carrito/', views.Carrito, name='carrito')
]
