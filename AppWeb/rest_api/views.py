from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from GigaGames.models import Juego, Categoria
from .serializers import JuegoSerializer, CategoriaSerializer

# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_juegos(request):
    if request.method == 'GET':
        juego = Juego.objects.all()
        serializer = JuegoSerializer(juego, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser(). parse(request)
        serializer = JuegoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        


@csrf_exempt
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def vista_juegos(request, id):
    try:
        juego = Juego.objects.get(id=id)
    except Juego.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = JuegoSerializer(juego)
        return Response(serializer.data)
    
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = JuegoSerializer(juego, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        


        
    elif request.method == 'DELETE':
        juego.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@csrf_exempt
@api_view(['GET', 'POST'])
def lista_categorias(request):
    if request.method == 'GET':
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser(). parse(request)
        serializer = CategoriaSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        


@csrf_exempt
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def vista_categorias(request, id):
    try:
        categoria = Categoria.objects.get(id=id)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        


        
    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

