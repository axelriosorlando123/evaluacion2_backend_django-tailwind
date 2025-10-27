from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from .models import Cliente
from .forms import ClienteForm

# Listar clientes
def cliente_lista(request):
    clientes = Cliente.objects.order_by('-created_at')
    return render(request, 'catalogo/cliente_lista.html', {'clientes': clientes})

# Crear cliente
def cliente_crear(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente registrado con éxito ✅")
            return redirect('cliente_lista')
    else:
        form = ClienteForm()
    return render(request, 'catalogo/cliente_crear.html', {'form': form})

# Editar cliente
def cliente_editar(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente actualizado correctamente ✏️")
            return redirect('cliente_lista')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'catalogo/cliente_editar.html', {'form': form, 'cliente': cliente})

# Eliminar cliente
def cliente_eliminar(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.success(request, "Cliente eliminado correctamente 🗑️")
    return redirect('cliente_lista')
