from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from .models import Producto
from .forms import ProductoForm

@login_required

def producto_lista(request):
    productos = Producto.objects.order_by('-created_at')
    return render(request, 'catalogo/producto_lista.html', {'productos': productos})

def producto_crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado con éxito ✅")
            return redirect('producto_lista')
        else:
            print("❌ Errores del formulario:", form.errors)
            messages.error(request, f"Error al guardar: {form.errors}")
    else:
        form = ProductoForm()
    return render(request, 'catalogo/producto_crear.html', {'form': form})

def producto_eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto eliminado correctamente 🗑️")
    return redirect('producto_lista')

def producto_editar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado con éxito ✏️")
            return redirect('producto_lista')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'catalogo/producto_editar.html', {'form': form, 'producto': producto})