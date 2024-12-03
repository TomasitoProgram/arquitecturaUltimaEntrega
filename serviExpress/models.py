from django.contrib.auth.hashers import make_password
from django.db import models



class Vehiculo(models.Model):
    patente = models.CharField(max_length=6)
    marca = models.CharField(max_length=70)
    modelo = models.CharField(max_length=60)
    
    def __str__(self):
        return self.patente

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    password = models.CharField(max_length=255, default='')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.nombre
    
class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('procesada', 'Procesada'),
        ('enviada', 'Enviada'),
        ('completada', 'Completada')
    ], default='pendiente')
    costo = models.IntegerField()

    def __str__(self):
        return f"Orden #{self.id} - {self.cliente.nombre}"

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class ElementoOrden(models.Model):
    orden = models.ForeignKey(Orden, related_name='elementos', on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en Orden #{self.orden.id}"

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    
