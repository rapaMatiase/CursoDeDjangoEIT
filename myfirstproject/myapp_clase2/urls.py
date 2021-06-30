
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/', views.myFirstTemplate, name='user_perfil'),
    path('e1/', views.ejercicio1, name='ejericicio1'),
    path('e2/', views.ejercicio2, name='ejericicio2'),
    path('e3/', views.ejercicio3, name='ejericicio3'),
    path('e4/', views.ejercicio4, name='ejericicio4'),
    path('e5/', views.ejercicio5, name='ejericicio5'),

    path('compras/', views.compras, name='compras'),
    path('facebook/', views.facebook, name='facebook'),
    path('ordenes/', views.ordenes, name='ordenes'),


]

