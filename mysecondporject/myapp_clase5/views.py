from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Album, Artista, Cancion
# Create your views here.

def index(request):
    albunes = Album.objects.all()

    return render(
        request,
        "myapp_clase5/index.html",
        context={'albunes' : albunes}
    )

def album(request, album_id):
    album = Album.objects.get(id = album_id)
    canciones = Cancion.objects.filter(album = album)
    return render(
        request,
        "myapp_clase5/album.html",
        context={
            'album' : album,
            'canciones' : canciones
            }
    )


def artista(request, artista_id):
    artista = Artista.objects.get(id = artista_id)
    print(artista.album_set.all())
    return render(
        request,
        "myapp_clase5/artistas.html",
        context={'artista': artista}
    )