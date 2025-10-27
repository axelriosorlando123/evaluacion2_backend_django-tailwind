from django.db import models
from django.utils import timezone
import uuid

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)  # ← sin unique=True
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, default='Sin categoría')
    precio = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} (${self.precio})"
    
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    total_gastado = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return f"{self.nombre} ({self.rut})"

    
    
class DetalleVenta(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='detalles')
    cantidad = models.PositiveIntegerField(default=1)
    
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
        null=True,
        blank=True
    )
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False,
        default=0,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.producto:
            self.precio = self.producto.precio
        self.subtotal = (self.precio or 0) * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Detalle de {self.producto} (x{self.cantidad})"
