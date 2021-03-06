from django.shortcuts import redirect, render
from .forms import MyFilesForm, AcceptForm
from .models import MyFiles, Estadistica, Value
from .Convert import ConvertCsvToList, DeleteFile, ConvertCsvToListWithoutHeaders
# Create your views here.

def UpdateView(request):

    #Instancia vacia de mi fromulario
    form = MyFilesForm()

    #Cuando me envian un formulario completo.
    if request.method == 'POST':
        # Ahora tebgo un formulario pero lleno con lo enviado por el usuario
        form = MyFilesForm(request.POST, request.FILES)
        if form.is_valid():
            # No solo guardo en BD, me quedo con una  instancia para manipular ahora.
            newMyFile = form.save()
            return redirect(
                'data_show', 
                file_id=newMyFile.id
                )
        
    return render(
        request,
        "excel/update.html",
        context={'form': form}
    )

def DataShowView(request, file_id):

    myfile = MyFiles.objects.get(id = file_id)
    lista = ConvertCsvToList(myfile.file)
    form = AcceptForm()

    if request.method == 'POST':
        if 'Volver' in request.POST:
            #Borrar el archvio de media
            DeleteFile(myfile.file)
            #Borro de la base de datos
            myfile.delete()

            return redirect('update')

        if 'Aceptar' in request.POST:
            form = AcceptForm(request.POST)

            if form.is_valid():
                return redirect(
                    'data_save', 
                    file_id=file_id
                    )
    

    return render(
        request,
        "excel/datashow.html",
        context={
            'file_id' : file_id,
            'headers' : lista[0],
            'lista_paices_poblacion': lista[1:],
            'form': form
            }
    )

def SaveData(request, file_id):
    myfile = MyFiles.objects.get(id = file_id)
    diccionario = ConvertCsvToListWithoutHeaders(myfile.file)
    
    estadistica = Estadistica(name='Nombre ramdom')
    estadistica.save()
    print(diccionario)
    for pais in diccionario:
        value = Value(name=pais['pais'], value=pais['poblacion'], estadistica = estadistica)
        value.save()

    return render(
        request,
        "excel/save.html",
        context={
            'file_id' : file_id,
        }
    )