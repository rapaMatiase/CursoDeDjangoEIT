from django.contrib import admin
from django.db.models import fields
from .models import Artista, Album, Cancion
# Register your models here.

class ArtistaAdmin(admin.ModelAdmin):
    # Hace referencia a los campos que mostramos en el admin
    #fields = ['nombre', 'apellido', 'nombreArtistico','nacionalidad']
    # Hace solo lectura los campos que aparecen en la lista de fields y readonly_fields simultaneamente
    readonly_fields = ['nacionalidad']
    fieldsets = (
        ('Datos personales', {
            'fields': ('nombre', 'apellido')
        }),
        ('Datos artisticos',{
            'fields' : ('nombreArtistico', 'fechaDeNacimiento')
        })
    )

class AlbumAdmin(admin.ModelAdmin): 
    readonly_fields = ['fechaDeLanzamiento']
    list_display = ('nombre', 'fechaDeLanzamiento')
    list_filter = ['nombre', 'fechaDeLanzamiento']
    ordering = ['id']
    
    class Meta:
        model = Album
        fields = '__all__'

admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Cancion)

