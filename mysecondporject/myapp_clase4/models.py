from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
List todo
"""


class List(models.Model):
    # El orm tmb crea un campo de id
    # Es para un campo de texto, en la bd se convierte creo VARCHAR
    title = models.CharField(max_length=30)
    # Quiero especificar cuando fue creada la lista
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    # Queiro especificaar cuando fue la ultima modificacion
    date_update = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

"""
EJERCICIO 1
Para el modelo item, crear un campo de texto de 200 caracteres llamado detail, y definir
dos campos de fecha, uno para guardar el momento de creacion y otro para guardar la ultima actualizacion. Utilizar el modelo List como ejemplo.
Crear 2 o 3 items por el shell y una vista donde verlos.
HASTA 11.08
"""

class Item(models.Model):
    detail = models.CharField(max_length=200)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True)

"""
EJERCICIO 2
Plantear un modelo para el siguiente negocio.
Dado un banco, cada usuario tiene una cta cte en pesos.

"""

class CtaCte(models.Model):

    BADGE_LIST = [ 
        ('D', 'Dolares'),
        ('P', 'Pesos')
        ]

    user = models.ForeignKey(User, on_delete=models.Case)
    mount = models.FloatField()
    badge = models.CharField(
        max_length=20,
        choices=BADGE_LIST, 
        default='Dolares'
        )