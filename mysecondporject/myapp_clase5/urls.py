
from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/<int:album_id>', views.album, name='album'),
    path('artista/<int:artista_id>', views.artista, name='artista')
]
