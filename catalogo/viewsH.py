from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Sum, Count
from .models import Producto
from .models import DetalleVenta  

@login_required
def home(request):
    # Productos más vendidos
    productos_vendidos = (
        DetalleVenta.objects
        .values('producto__nombre')
        .annotate(total_vendido=Sum('cantidad'))
        .order_by('-total_vendido')[:5]
    )

    # Clientes con más ventas
    clientes_top = (
        DetalleVenta.objects
        .values('cliente__nombre')
        .annotate(total_compras=Count('id'))
        .order_by('-total_compras')[:5]
    )

    context = {
        'productos_vendidos': productos_vendidos,
        'clientes_top': clientes_top,
    }
    return render(request, 'catalogo/home.html', context)
