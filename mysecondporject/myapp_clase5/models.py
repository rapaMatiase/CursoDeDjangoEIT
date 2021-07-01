from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nombreArtistico = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    fechaDeNacimiento = models.DateTimeField()

    def __str__(self):
        return "{}, {}".format(self.apellido, self.nombre)

class Album(models.Model):
    nombre = models.CharField(max_length=50)
    fechaDeLanzamiento = models.DateTimeField()
    artistas = models.ManyToManyField(Artista)

    def __str__(self):
        return "{}".format(self.nombre)

class Cancion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nombre)