from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('explorar/', explorar, name="explorar"),
    path('categoria/', categoria, name="categoria"),


    path('j/<int:id>', juego, name="juego"),
    path('mantenedor/agregar_juego/', agregar_juego, name="agregar_juego"),
    
]
