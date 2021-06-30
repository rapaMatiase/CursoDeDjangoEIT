from django.shortcuts import render

# Create your views here.

"""
EJERICICO 4 - MODIFICADO CON EL BONUS
Dada una lista de articulos. Crear una vista que los muestre en una lista y
en cada item que no tenga stock disponible, colorear de color rojo. 
"""

articulos = {
    'articulos' : [
        { 'number' : 1, 'name' : 'Cuchillo', 'stock' : 0},
        { 'number' : 2, 'name' : 'Balanza', 'stock' : 2},
        { 'number' : 3, 'name' : 'Computadora', 'stock' : 0},
        { 'number' : 4, 'name' : 'Lampara', 'stock' : 23}
    ]
}

def ejercicio4(request):
    return render(request, 'myapp_clas2_bonus/mercadolibre.html', articulos)