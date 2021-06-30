from django.shortcuts import redirect, render
from .forms import FormularioLogin, FormularioArticulo

# Create your views here.
def index(request):
    return render(
        request,
        'myapp_clase3/index.html',
        context={
            'nombre':'Ezequiel',
            'estado' : 'al dia'
            }
    )

listaDeOrdenes = {
    'ordenes' : [
        {'id' : 1, 'state' : 'Saliendo', 'detail':'El cliente solicito ...'},
        {'id' : 2, 'state' : 'en preparacion', 'detail':'El vendedor '},
        {'id' : 3, 'state' : 'en espera', 'detail':'El deudor '},
        {'id' : 4, 'state' : 'Saliendo', 'detail':'El acredor'},
    ]
}

def detail(request, id):
    """
        Muestra el detalle de una orden en particular
    """
    ordenBuscada = None
    for orden in listaDeOrdenes['ordenes']:
        if orden['id'] == id:
            ordenBuscada = orden
    return render(
        request,
        'myapp_clase3/detail.html',
        ordenBuscada
    )

def list(request):
    """
        Muestra la lista de todas las ordenes.
    """
    return render(
        request,
        'myapp_clase3/list.html',
        context=listaDeOrdenes
    )


"""
EJERCICIO 1
Dado una lista de articulos. Crear dos vistas, una con la lista de articulos y otra con el 
detalle de los articulos. Enlazar una con la otra por medio de una url dinamica. 
"""

articulos = {
    'articulos':[
        {'id' : 1, 'name' : 'tornillo', 'price':'500'},
        {'id' : 2, 'name' : 'clavo', 'price':'530'},
    ]
}

def detailArticulos(request, id):
    articuloBuscado = None
    
    for articulo in articulos['articulos']:
        if articulo['id'] == id:
            articuloBuscado = articulo

    return render(
        request,
        'myapp_clase3/detail_articulos.html',
        articuloBuscado
    )

def listArticulos(request):
    return render(
        request,
        'myapp_clase3/list_articulos.html',
        articulos
    )

""""
EJERICICO 2

Agregar a los templates de las vistas de articulos un html base con
un mismo header y dististintos titulos y contenido.
"""

def form(request):
    # Declaro un nuevo formulario
    form = FormularioLogin()

    #Si es Post quiero un formulario con los valores ingresados por el usuario y los errores
    if request.method == 'POST':
        """
            Siempre primero controlo el methodo, porque si es get, es
            la primera vez que ingresa en la url.
        """
        #Obtengo los datos del POST
        form = FormularioLogin(request.POST)
        if form.is_valid():
            return redirect('list')

    return render(
        request,
        'myapp_clase3/form.html',
        context= {'form' : form}
        )

def formArtiuclo(request):
    form = FormularioArticulo()

    if request.method == 'POST':
        form = FormularioArticulo(request.POST)
        if form.is_valid():
            return redirect('list_articulos')

    return render(
        request,
        'myapp_clase3/formArticulo.html',
        {'form':form}
    )