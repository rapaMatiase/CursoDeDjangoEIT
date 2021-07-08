from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Item(models.Model):
    detail = models.CharField(max_length=200)
    data_create = models.DateField(auto_now_add=True)