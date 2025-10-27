from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import DetalleVenta

# 🔹 Cuando se crea o actualiza un detalle, recalculamos el total gastado del cliente
@receiver(post_save, sender=DetalleVenta)
def actualizar_total_cliente(sender, instance, **kwargs):
    total = sum([d.subtotal for d in instance.cliente.detalles.all()])
    instance.cliente.total_gastado = total
    instance.cliente.save(update_fields=['total_gastado'])

# 🔹 Cuando se elimina un detalle
@receiver(post_delete, sender=DetalleVenta)
def recalcular_total_cliente_al_eliminar(sender, instance, **kwargs):
    total = sum([d.subtotal for d in instance.cliente.detalles.all()])
    instance.cliente.total_gastado = total
    instance.cliente.save(update_fields=['total_gastado'])

