from django.shortcuts import render, redirect, get_object_or_404
from .forms import JuegoForm
from .models import Juego
# Create your views here.


def home(request):
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

def modificar_juego_lista(request):

    juegos = Juego.objects.all()

    data = {
        'juegos' : juegos
    }

    return render(request, "mantenedor/juego/listado_juegos.html", data)


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


def eliminar_juego(request, idjuego):

    juego = get_object_or_404(Juego, id = idjuego)

    juego.delete()

    return redirect(to="modificar_juego_lista")