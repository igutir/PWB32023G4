from django.urls import path
from .views import *
from django.contrib.auth.views import (LoginView, 
                                       LogoutView, 
                                       PasswordChangeView, 
                                       PasswordChangeDoneView, 
                                       PasswordResetView, 
                                       PasswordResetDoneView, 
                                       PasswordResetConfirmView, 
                                       PasswordResetCompleteView)

urlpatterns = [ 

    path('', home, name="home"),
    path('explorar/', explorar, name="explorar"),
    path('categoria/', categoria, name="categoria"),
    path('categoria/<int:id>', categoria, name="categoria"),

    ##para la api, es un ejemplo
    path('api_rickandmorty/', api_rickandmorty, name="api_rickandmorty"),

    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('registro_usuario/', registro_usuario, name="registro_usuario"),
    path("password_change/", PasswordChangeView.as_view(template_name="pw/password_change_form.html"), name="password_change"),
    path("password_change/done/", PasswordChangeDoneView.as_view(template_name="pw/password_change_done.html"), name="password_change_done"),
    path("password_reset/", PasswordResetView.as_view(template_name="pw/password_reset_form.html", email_template_name='pw/password_reset_email.html'), name="password_reset"),
    path("password_reset/done/", PasswordResetDoneView.as_view(template_name="pw/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name="pw/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", PasswordResetCompleteView.as_view(template_name="pw/password_reset_complete.html"), name="password_reset_complete"),

   # path("perfil/", vistaMostrarPerfil.as_view(), name="perfil"),
    path("perfil/", editar_perfil, name="editar_perfil"),

    path('j/<int:id>/', juego, name="juego"),
    path('mantenedor/', mantenedor_juegos, name="mantenedor_juegos"),
    path('mantenedor/agregar_juego/', agregar_juego, name="agregar_juego"),
    path('mantenedor/listado_juegos/', modificar_juego_lista, name="modificar_juego_lista"),
    path('mantenedor/listado_juegos/u/<int:idjuego>/', modificar_juego, name="modificar_juego"),
    path('mantenedor/listado_juegos/d/<idjuego>/', eliminar_juego, name="eliminar_juego"),
    











    







]
