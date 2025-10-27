from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from .models import DetalleVenta
from .forms import DetalleVentaForm

def detalleventa_lista(request):
    detalles = DetalleVenta.objects.order_by('-created_at')
    return render(request, 'catalogo/detalleventa_lista.html', {'detalles': detalles})

def detalleventa_crear(request):
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Detalle de venta agregado con éxito 🧾")
            return redirect('detalleventa_lista')
    else:
        form = DetalleVentaForm()
    return render(request, 'catalogo/detalleventa_crear.html', {'form': form})

def detalleventa_editar(request, id):
    detalle = get_object_or_404(DetalleVenta, id=id)
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST, instance=detalle)
        if form.is_valid():
            form.save()
            messages.success(request, "Detalle de venta actualizado correctamente ✏️")
            return redirect('detalleventa_lista')
    else:
        form = DetalleVentaForm(instance=detalle)
    return render(request, 'catalogo/detalleventa_editar.html', {'form': form, 'detalle': detalle})

def detalleventa_eliminar(request, id):
    detalle = get_object_or_404(DetalleVenta, id=id)
    detalle.delete()
    messages.success(request, "Detalle de venta eliminado correctamente 🗑️")
    return redirect('detalleventa_lista')
