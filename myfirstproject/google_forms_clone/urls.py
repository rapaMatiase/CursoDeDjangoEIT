from django.urls import path
from . import views

#path('url a escribir en el browser/', vista, name de url)
urlpatterns = [
    path('form/', views.formulario, name='formulario'),
]
