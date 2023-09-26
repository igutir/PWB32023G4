from django.shortcuts import render
from .forms import JuegoForm
from .models import Juego
from django.shortcuts import get_object_or_404
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
            data["form_contacto"] = formulario

    return render(request, "mantenedor/juego/agregar.html", data)

