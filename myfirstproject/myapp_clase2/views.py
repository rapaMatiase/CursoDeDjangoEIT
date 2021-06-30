from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Repaso")

perfil = {
    'name' : 'Ezequiel',
    'lastname' : 'rapa',
    'age' : 28
}

def myFirstTemplate(request):
    return render(request, 'myapp_clase2/perfil.html', perfil)

"""
EJERCICIO 1
Dada una variable que representa el detalle de los datos de un articulo
de mercado libre. Crear una vista con template para mostrar al usuario.
HASTA 10.34 
"""

articulo = {
    'number' : '221314',
    'price' : 500,
    'detail' : 'Excelente cuchillo para coicnar',
    'brand' : 'AceroDX',
    'stock' : 20
}

def ejercicio1(request):
    return render(request, 'myapp_clase2/detail.html', articulo)

"""
EJERCICIO2
Dado una variable que representa el estado de cuenta de un usuario en un banco.
Crear una vista con un tamplate que muestre sus datos y el monto de su cuenta.
Si monto de la cuenta es negativo que se muestre el numero de color rojo,
si no de color verde.
HASTA 10.53
"""

banco = {
    'name' : 'Matias',
    'ctacte': -2323
}

def ejercicio2(request):
    return render(request, 'myapp_clase2/banco.html', banco)
#return render(request, 'template', contexto(datos))


listaDeCompras = {
    'responsable' : 'Matias',
    'lista' : ['Tomate', 'Lechuga', 'Coca', 'Cepillo de dientes']
}

def compras(request):
    return render(request, 'myapp_clase2/compras.html', listaDeCompras)


"""
Dada una variable que representa la lista de amigos de facebook. Creara un
vista con template que los muestre en una lista de ul.
HASTA 11.09
"""

perfil_facebook = {
    'username' : 'Matias',
    'friends' : ['Marcelo', 'Gonzalo', 'Lucia', 'Ignacio', 'David']
}

def ejercicio3(request):
    return render(request, 'myapp_clase2/facebook.html', perfil_facebook)

perfil_facebook = {
    'username' : 'Matias',
    'friends' : [
        {'username':'Marcelo', 'state': 'activo'},
        {'username':'Gonzalo', 'state': 'activo'} ,
        {'username':'Lucia', 'state': 'inactivo'},
        {'username':'Ignacio', 'state': 'bloquedo'}, 
        {'username':'David', 'state': 'activo'},
    ]
}

def facebook(request):
    return render(request, 'myapp_clase2/facebook2.html', perfil_facebook)

"""
EJERICICO 4
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
    return render(request, 'myapp_clase2/mercadolibre.html', articulos)

listaDeOrdenes = {
    'ordenes' : [
        {'number' : 1, 'state' : 'entregada'},
        {'number' : 2, 'state' : 'despachando'},
        {'number' : 3, 'state' : 'mesa de entrada'},
        {'number' : 4, 'state' : 'despachando'},
        {'number' : 5, 'state' : 'mesa de entrada'},
    ]
}

def ordenes(request):
    listaOrdenesFiltradas = {
        'entregadas' : [],
        'despachando' : [],
        'mesaDeEntrada' : []
    }
    for orden in listaDeOrdenes['ordenes']:
        
        if orden['state'] == 'entregada':
            listaOrdenesFiltradas['entregadas'].append(orden)
        elif orden['state'] == 'despachando':
            listaOrdenesFiltradas['despachando'].append(orden)
        else:
            listaOrdenesFiltradas['mesaDeEntrada'].append(orden)
    print(listaOrdenesFiltradas)


    return render(
        request, 
        'myapp_clase2/ordenes.html', 
        context= {
            'listaDeOrdenes' : listaDeOrdenes,
            'listaOrdenesFiltradas' : listaOrdenesFiltradas
            }
        )

"""
Utilizando la varaible perfil_facebook. Crear una vista con template donde
se cree una lista con los amigos activos, otra con los inactivos y una ultima
con los bloqueados.

Hacer el filtro donde lo crea mas conveniente.
"""

perfil_facebook = {
    'username' : 'Matias',
    'friends' : [
        {'username':'Marcelo', 'state': 'activo'},
        {'username':'Gonzalo', 'state': 'activo'} ,
        {'username':'Lucia', 'state': 'inactivo'},
        {'username':'Ignacio', 'state': 'bloquedo'}, 
        {'username':'David', 'state': 'activo'},
    ]
}

def ejercicio5(request):
    
    activos = []
    inactivos = []
    bloqueados = []
    
    for user in perfil_facebook['friends']:
        if user['state'] == 'activo':
            activos.append(user)
        elif user['state'] == 'inactivo':
            inactivos.append(user)
        elif user['state'] == 'bloquedo':
            bloqueados.append(user)

    return render(
        request, 
        'myapp_clase2/perfilFiltrado.html', 
        context = {
            'username' : perfil_facebook['username'],
            'activos' : activos,
            'inactivos' : inactivos,
            'bloqueados' : bloqueados
        }
        )