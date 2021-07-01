from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Compra, Articulo, ArticuloPorCompra
# Create your views here.

def Carrito(request):
    articulos = Articulo.objects.all()
    return render(
        request,
        "myapp_clase5_bonus/carrito.html",
        context={'articulos' : articulos }
    )

def Comprar(request):
    """
        Obtener un form con los artiuclos solicitados
    """
    # ESTO ESTA MUY MAL, PERO ES PARA PROBAR LAS CONSULTAS!!!
    
    articulos_comprados = [1, 2]
    compra = Compra()
    compra.save()

    for articuloComprado in articulos_comprados:
        articulo = Articulo.objects.get(id = articuloComprado)
        ac = ArticuloPorCompra(
            precio_compra = articulo.precio,
            articulo = articulo,
            compra = compra
        )
        ac.save()

    return render(
        request,
        "myapp_clase5bonus/compras.html",
        context={}
    )
