from django.db import models

# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(max_length=50)

class Articulo(models.Model):
    nombre = models.CharField(max_length=60)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    date = models.DateTimeField(auto_now=True)
    articulos = models.ManyToManyField(Articulo, through='ArticuloPorCompra')

class ArticuloPorCompra(models.Model):
    precio_compra = models.FloatField()
    cantidad = models.IntegerField(default=1)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)