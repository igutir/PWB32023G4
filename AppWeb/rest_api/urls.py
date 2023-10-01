from django.urls import path
from . import views



#api/
urlpatterns = [
    path('juegos/', views.lista_juegos, name='lista_juegos'),
    path('juegos/<id>', views.vista_juegos, name='vista_juegos'),

    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/<id>', views.vista_categorias, name='vista_categorias')
            ]