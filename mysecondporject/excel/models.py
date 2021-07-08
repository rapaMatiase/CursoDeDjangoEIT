from django.db import models

# Create your models here.
class MyFiles(models.Model):
    name = models.CharField(max_length=50)
    update = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='files/')


class Estadistica(models.Model):
    #id --> que invisible
    name = models.CharField(max_length=50)

class Value(models.Model):
    name = models.CharField(max_length=50)
    value = models.FloatField()
    estadistica = models.ForeignKey(
        Estadistica, 
        on_delete=models.CASCADE
        )