from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserChangeForm, UserModel
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.contrib import messages

from django.views import generic

from django.urls import reverse_lazy

from .forms import JuegoForm, ActualizarPerfilForm, ActualizarUsuarioForm
from .models import Juego, Categoria

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

    juegos_categoria = Juego.objects.filter(Categoria_id =id)

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





##ejemplo para la api
def api_rickandmorty(request):
    url = "https://rickandmortyapi.com/api/character"
    response = requests.get(url)

    personajes = response.json().get('results',[])

    context = {
        'personajes': personajes

    }
    return render(request, 'api_rickandmorty.html', context)






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





def editar_perfil(request):

    data = {
        "mensaje": ""
    }

    if request.method == "POST":
        usuario_form = ActualizarUsuarioForm(request.POST, instace=request.user)
        perfil_form = ActualizarPerfilForm(request.POST, instance=request.user.perfil)

        if usuario_form.is_valid() and perfil_form.is_valid():
            usuario_form.save()
            perfil_form.save()

            data["mensaje"] = "Datos actualizados correctamente"

            return redirect(to="perfil")
        
    else:
        usuario_form = ActualizarUsuarioForm(instance=request.user)
        perfil_form = ActualizarPerfilForm(instance=request.user.perfil)

    return render(request, 'registration/editar_perfil.html', {'usuario_form': usuario_form, 'perfil_form': perfil_form})


