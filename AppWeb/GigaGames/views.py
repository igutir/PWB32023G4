from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.models import User, Group

from django.contrib import messages

from .forms import JuegoForm
from .models import Juego


# Create your views here.


def home(request):

    # messages.success(request, "msj")

    request.session["mensaje"] = "Hola"

    return render(request, "index.html")

def categoria(request):
    return render(request, "categoria.html")

def explorar(request):

    juegos = Juego.objects.all()

    data = {
        'juegos' : juegos
    }

    return render(request, "explorar.html", data)

def juego(request, id):

    juego = get_object_or_404(Juego, id = id)

    data = {
        'juego' : juego
    }

    return render(request, "juego.html", data)

@login_required(login_url="/accounts/login/")
@permission_required(['GigaGames.add_juego'], login_url="/accounts/login/")
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

@login_required(login_url="/accounts/login/")
@permission_required(['GigaGames.change_juego', 'GigaGames.delete_juego'], login_url="/accounts/login/")
def modificar_juego_lista(request):

    juegos = Juego.objects.all()

    data = {
        'juegos' : juegos
    }

    return render(request, "mantenedor/juego/listado_juegos.html", data)

@login_required(login_url="/accounts/login/")
@permission_required(['GigaGames.change_juego'], login_url="/accounts/login/")
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

@login_required(login_url="/accounts/login/")
@permission_required(['GigaGames.delete_juego'], login_url="/accounts/login/")
def eliminar_juego(request, idjuego):

    juego = get_object_or_404(Juego, id = idjuego)

    juego.delete()

    return redirect(to="modificar_juego_lista")


def login_usuario(request):
    
    print('Bienvenido ' + request.user.username)

    if request.user.groups.filter(name="usuario"):
        print("Grupo: Usuario")

    return redirect(to="home")

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