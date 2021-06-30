from django.shortcuts import render, HttpResponse, redirect
from .models import CtaCte, List, Item
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return HttpResponse("Este es tu index!!!!")

list_friends = {
    'user' : "Matias",
    'friends' : [
        {'id': 1, 'name' : 'Lucia', 'state' : 'activate'},
        {'id': 2, 'name' : 'Gonzalo', 'state' : 'desactivate'},
        {'id': 3, 'name' : 'David', 'state' : 'activate'}
    ]
}

def ListFriends(request):
    return render(
        request,
        "myapp_clase4/list_friends.html",
        context=list_friends
    )


def ListListToDo(request, user_id):
    user = User.objects.get(id = user_id)
    lists = List.objects.filter(user = user)
    return render(
        request,
        "myapp_clase4/list_listtodo.html",
        context={'lists' : lists }
    )

def ListDetail(request, user_id, list_id):
    # Busco la intancia de la lista
    list = List.objects.get(id = list_id)
    # Depues utilizo esa instancia para buscar sus items.
    items_one_list = Item.objects.filter(list = list)
    return render(
        request,
        "myapp_clase4/list_detail.html",
        context={'items' : items_one_list, 'list_id': list_id,  'user_id' : user_id}
    )

def ListItemDelete(request, user_id, list_id, item_id):
    item = Item.objects.get(id = item_id)
    item.delete()
    return redirect(
        to='list_detail', 
        user_id = user_id, 
        list_id = list_id
    )

"""
EJERCICIO 4
Crear una vista para ver el monto de la cuenta del usuario
correspondiente al id recibido!!
"""

def CtaCteView(request, user_id):
    user = User.objects.get(id = user_id)
    ctacte = CtaCte.objects.filter(user = user)

    return render(
        request,
        "myapp_clase4/ctacte.html",
        context={'ctacte' : ctacte}
    )