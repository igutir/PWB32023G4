from typing import Any
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.contrib import messages

from django.contrib.auth.forms import UserChangeForm

from django.views.generic import UpdateView

from django.urls import reverse_lazy

from .forms import JuegoForm, ActualizarUsuarioForm, ActualizarPerfilForm
from .models import Juego, Categoria, Perfil

import requests

# Create your views here.


def home(request):

    # messages.success(request, "msj")
    #request.session["mensaje"] = "Hola"

    juegos_carrusel = Juego.objects.filter(imagen_carrusel__startswith="cover/carrusel/")

    data = {
        'juegos' : juegos_carrusel
    }

    return render(request, "index.html", data)

def categoria(request, id):

    categoria = get_object_or_404(Categoria, id = id)

    juegos_categoria = Juego.objects.filter(categoria_id=id)

    data = {
        'categoria' : categoria,
        'juegos_categoria' : juegos_categoria
    }

    return render(request, "categoria.html", data)

def explorar(request):

    juegos = Juego.objects.all()


    data = {
        'juegos' : juegos
    }

    return render(request, "explorar.html", data)





##Paginas para el pokemon
def pokedex_api(request):
    return render(request, 'pokedex_api.html')

def quepokemoneres(request):
    return render(request, 'quepokemoneres.html')






def juego(request, id):

    juego = get_object_or_404(Juego, id = id)

    data = {
        'juego' : juego
    }

    return render(request, "juego.html", data)


@login_required(login_url="login/")
@permission_required(['GigaGames.add_juego', 'GigaGames.delete_juego'], login_url="login/")
def mantenedor_juegos(request):

    return render(request, "mantenedor/juego/mantenedor_juegos.html")


@login_required(login_url="login/")
@permission_required(['GigaGames.add_juego'], login_url="login/")
def agregar_juego(request):

    data = {
        "form_juego": JuegoForm,
        "mensaje": ""
    } 

    if request.method == "POST":
        formulario = JuegoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid:
            formulario.save()
            data["mensaje"] = "Juego agregado"
        else:
            data["mensaje"] = "Error"
            data["form"] = formulario

    return render(request, "mantenedor/juego/agregar.html", data)

@login_required(login_url="login/")
@permission_required(['GigaGames.change_juego', 'GigaGames.delete_juego'], login_url="login/")
def modificar_juego_lista(request):

    juegos = Juego.objects.all()

    data = {
        'juegos' : juegos
    }

    return render(request, "mantenedor/juego/listado_juegos.html", data)

@login_required(login_url="login/")
@permission_required(['GigaGames.change_juego'], login_url="login/")
def modificar_juego(request, idjuego):

    juego = get_object_or_404(Juego, id = idjuego)

    data = {
        "form_juego": JuegoForm(instance=juego)
    } 

    if request.method == "POST":
        formulario = JuegoForm(data=request.POST, instance=juego, files=request.FILES)

        if formulario.is_valid:
            formulario.save()
            return redirect(to="modificar_juego_lista")
        else:
            data["mensaje"] = "Error"
            data["form"] = formulario

    return render(request, "mantenedor/juego/modificar.html", data)

@login_required(login_url="login/")
@permission_required(['GigaGames.delete_juego'], login_url="login/")
def eliminar_juego(request, idjuego):

    juego = get_object_or_404(Juego, id = idjuego)

    juego.delete()

    return redirect(to="modificar_juego_lista")


def login_usuario(request):
    
    print('Bienvenido ' + request.user.username)

    if request.user.groups.filter(name="usuario"):
        print("Grupo: Usuario")

    return render(request, "registration/login.html")

def editar_perfil(request):

    usuario = get_object_or_404(User, id = request.user.id)
    perfil = get_object_or_404(Perfil, user_id = request.user.id)

    print(perfil)

    data = {
        "form_user": ActualizarUsuarioForm(instance=usuario),
        "form_profile": ActualizarPerfilForm(instance=perfil)
    } 

    if request.method == "POST":
       
        form_usuario = ActualizarUsuarioForm(request.POST, instance=request.user)
        form_perfil = ActualizarPerfilForm(request.POST, instance=request.user.perfil)

        if form_usuario.is_valid and form_perfil.is_valid:
            
            form_usuario.save()
            form_perfil.save()


            return redirect(to="editar_perfil")
        else:

            form_usuario = ActualizarUsuarioForm(instance=request.user)
            form_perfil = ActualizarPerfilForm(instance=request.user.perfil)

            data['form_usuario'] = form_usuario
            data['form_perfil'] = form_perfil
            
    return render(request, 'registration/editar_perfil.html', data)

def registro_usuario(request):

    data = {
        "mensaje": ""
    }

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password = request.POST.get("password")

        usuario = User()
        usuario.set_password(password)
        usuario.username = nombre
        usuario.first_name = nombre
        usuario.last_name = apellido
        usuario.email = correo

        grupoUsuario = Group.objects.get(name="usuario")

        try:   
            usuario.save()
            usuario.groups.add(grupoUsuario)

            user = authenticate(username=usuario.username, password=password)
            login(request, user)

            return redirect(to="home")
        
        except:
            data["mensaje"] = "Hubo un error"

    return render(request, "registration/registro.html")


