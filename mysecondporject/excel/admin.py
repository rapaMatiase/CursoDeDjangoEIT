from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Estadistica, Value, MyFiles
# Register your models here.

class ValueAdmin(ModelAdmin):
    model= Value
    list_display = ['name', 'value']

admin.site.register(Estadistica)
admin.site.register(Value, ValueAdmin)
admin.site.register(MyFiles)



