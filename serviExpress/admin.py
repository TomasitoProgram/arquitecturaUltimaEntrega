from django.contrib import admin
from .models import Cliente, Orden, Servicio, ElementoOrden, Vehiculo

admin.site.register(Cliente)
admin.site.register(Orden)
admin.site.register(Servicio)
admin.site.register(ElementoOrden)
admin.site.register(Vehiculo)

