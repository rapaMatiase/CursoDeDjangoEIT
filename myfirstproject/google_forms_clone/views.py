from django.shortcuts import render

# Create your views here.




def formulario(request):
    """
        Un formuladio, y segun el valor de algun campo o mas,
        lo redirigir a otro formulario. 
    """

    return render(
        request,
        'google_forms_clone/form_1.html',
        context = {}
    )