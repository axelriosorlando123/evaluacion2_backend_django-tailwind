from django import forms
from .models import Producto,Cliente,DetalleVenta

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Teclado mecánico RGB',
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
            'categoria': forms.TextInput(attrs={
                'placeholder': 'Ej: Periféricos',
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
            'precio': forms.NumberInput(attrs={
                'step': '1',
                'placeholder': 'Ej: 19990',
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'correo', 'telefono', 'direccion']
        widgets = {
            'rut': forms.TextInput(attrs={
                'placeholder': 'Ej: 12.345.678-9',
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ej: Juan Pérez',
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
            'correo': forms.EmailInput(attrs={
                'placeholder': 'Ej: cliente@email.com',
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
            'telefono': forms.TextInput(attrs={
                'placeholder': 'Ej: +56 9 1234 5678',
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
            'direccion': forms.TextInput(attrs={
                'placeholder': 'Ej: Av. Siempre Viva 742',
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
        }
                
class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['cliente', 'producto', 'cantidad']
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
            'producto': forms.Select(attrs={
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
            'cantidad': forms.NumberInput(attrs={
                'placeholder': 'Ej: 1',
                'class': 'border rounded px-3 py-2 w-full focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }),
        }