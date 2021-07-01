from django.db import models

# Create your models here.


class Excel(models.model):
    excel = models.FileField()
    