from django.shortcuts import render, redirect

from .cart import Cart
from GigaGames.models import Juego

def verCart(request):
    juegos = Juego.objects.all()

    data = {
        'juegos' : juegos
    }
    
    print(juegos)

    return render(request, 'cart.html', data)

def agregarJuegoCart(request, id):
    carro = Cart(request)
    juego = Juego.objects.get(id=id)

    carro.agregar(juego)

    return redirect(to="ver_cart")

def disminuirJuegoCart(request, id):
    carro = Cart(request)
    juego = Juego.objects.get(id=id)
    
    carro.disminuir(juego)

    return redirect(to="ver_cart")

def eliminarJuegoCart(request, id):
    carro = Cart(request)
    juego = Juego.objects.get(id=id)
    
    carro.eliminar(juego)

    return redirect(to="ver_cart")

def limpiarCart(request):
    carro = Cart(request)
    carro.limpiar()

    return redirect(to="ver_cart")
