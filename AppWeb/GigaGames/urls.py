from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('explorar/', explorar, name="explorar"),
    path('categoria/', categoria, name="categoria"),


    path('j/<int:id>/', juego, name="juego"),
    path('mantenedor/agregar_juego/', agregar_juego, name="agregar_juego"),
    path('mantenedor/listado_juegos/', modificar_juego_lista, name="modificar_juego_lista"),
    path('mantenedor/listado_juegos/u/<int:idjuego>/', modificar_juego, name="modificar_juego"),
    path('mantenedor/listado_juegos/d/<idjuego>/', eliminar_juego, name="eliminar_juego"),

    path('login_usuario/', login_usuario, name="login_usuario"),

    path('registro_usuario/', registro_usuario, name="registro_usuario"),
]
