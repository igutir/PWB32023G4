from django.urls import path
from .views import *

urlpatterns = [
    path('', verCart, name='ver_cart'),
    path('agregar/<int:id>', agregarJuegoCart, name='agregar_cart'),
    path('disminuir/<int:id>', disminuirJuegoCart, name='disminuir_cart'),
    path('eliminar/<int:id>', eliminarJuegoCart, name='eliminar_cart'),
    path('limpiar/', limpiarCart, name='limpiar_cart'),
]
