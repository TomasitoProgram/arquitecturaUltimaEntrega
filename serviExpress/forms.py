from django import forms
from .models import Cliente, Orden, ElementoOrden

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'vehiculo', 'password']  # Incluye el campo password si es necesario

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Si necesitas realizar configuraciones adicionales en los campos, lo puedes hacer aquí
        self.fields['password'].widget = forms.PasswordInput()  # Hacer que el campo de contraseña sea un input tipo 'password'
        
class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['cliente', 'estado', 'costo']
        
class ElementoOrdenForm(forms.ModelForm):
    class Meta:
        model = ElementoOrden
        fields = ['orden', 'servicio', 'cantidad', 'precio_unitario']
        
        