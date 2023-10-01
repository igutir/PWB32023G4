from rest_framework import serializers
from GigaGames.models import Categoria, Compania, Juego

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Juego
        fields = ['nombre', 'descripcion', 'imagen', 'imagen_carrusel', 'precio', 'stock', 'Categoria', 'compania']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields = ['nombre']




       