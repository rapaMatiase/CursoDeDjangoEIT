from django.shortcuts import render, HttpResponse

# Create your views here.
def myview(request):
    return HttpResponse("Hola, esta es otra app")