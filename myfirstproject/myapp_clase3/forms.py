from django import forms
from django.forms.fields import CharField

"""
Documentacion
https://docs.djangoproject.com/en/3.2/ref/forms/fields/
"""

class FormularioLogin(forms.Form):
    # Campo de texo
    nombre = forms.CharField(max_length=5)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

"""
Crear un formuladio donde el usuario ingresa el nombre
 de un articulo, el precio y el stock. Que sean todos
 archivos de texto.

"""

class FormularioArticulo(forms.Form):
    nombre = forms.CharField(
                        max_length=50, 
                        required=False, 
                        label="Mega Nombre"
                        )
    precio = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'style' : 'border : red solid 4px'
                }
        )
        )
    stock = forms.CharField(max_length=50)
    descripcion = forms.CharField(
        max_length=300, 
        widget=forms.Textarea(
            attrs={
                'style' : 'color : red;'
            }
        )
        )

"""
Ejericio 5
Especificar un campo con widget del tipo textarea y agregar algun
atributo a gusto. 
"""