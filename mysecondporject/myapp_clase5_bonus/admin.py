from django.contrib import admin
from .models import Compra, Articulo, ArticuloPorCompra, Marca
# Register your models here.


admin.site.register(Compra)
admin.site.register(Articulo)
admin.site.register(ArticuloPorCompra)
admin.site.register(Marca)

