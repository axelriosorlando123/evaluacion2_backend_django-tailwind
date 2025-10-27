from django.urls import path
from . import viewsP, viewsC, viewsDV, viewsH

urlpatterns = [
    #home
    path('', viewsH.home, name='home'),
    #productos
    path('producto', viewsP.producto_lista, name='producto_lista'),
    path('producto/crear/', viewsP.producto_crear, name='producto_crear'),
    path('producto/editar/<int:id>/', viewsP.producto_editar, name='producto_editar'),
    path('producto/eliminar/<int:id>/', viewsP.producto_eliminar, name='producto_eliminar'),
    #clientes
    path('clientes/', viewsC.cliente_lista, name='cliente_lista'),
    path('clientes/crear/', viewsC.cliente_crear, name='cliente_crear'),
    path('clientes/editar/<int:id>/', viewsC.cliente_editar, name='cliente_editar'),
    path('clientes/eliminar/<int:id>/', viewsC.cliente_eliminar, name='cliente_eliminar'),
    #detallesventa
    path('detalles/', viewsDV.detalleventa_lista, name='detalleventa_lista'),
    path('detalles/crear/', viewsDV.detalleventa_crear, name='detalleventa_crear'),
    path('detalles/editar/<int:id>/', viewsDV.detalleventa_editar, name='detalleventa_editar'),
    path('detalles/eliminar/<int:id>/', viewsDV.detalleventa_eliminar, name='detalleventa_eliminar'),
]
