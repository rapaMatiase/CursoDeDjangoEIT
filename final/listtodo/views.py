from django.shortcuts import redirect, render
from .models import Item
from .forms import ItemForm
# Create your views here.

def Index(request):
    """
    Mostrar todas las tareas y un formulario para agregar tareas
    """
    items = Item.objects.all()
    
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            #Es para que el formulario este vacio
            form = ItemForm()

    return render(
        request,
        'listtodo/index.html',
        context={
            'items' : items,
            'form' : form
        }
    )

def Delete(request, item_id):
    """
        Voy a borrar un item de la lista
    """

    item = Item.objects.get(id = item_id)
    item.delete()

    return redirect('index')


def Update(request, item_id):
    item = Item.objects.get(id=item_id)
    form = ItemForm(instance=item)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(
        request,
        "listtodo/update.html",
        context={
            'form':form
        }
    )
