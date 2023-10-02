from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [ 

    path('', home, name="home"),
    path('explorar/', explorar, name="explorar"),
    #path('categoria/', categoria, name="categoria"),
    path('categoria/<int:id>', categoria, name="categoria"),

    ##Paginas para el pokemon
    path('pokedex_api/', pokedex_api, name="pokedex_api"),
    path('quepokemoneres/', quepokemoneres, name="quepokemoneres"),

    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('registro_usuario/', registro_usuario, name="registro_usuario"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="pw/password_change_form.html"), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="pw/password_change_done.html"), name="password_change_done"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="pw/password_reset_form.html", email_template_name='pw/password_reset_email.html'), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="pw/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="pw/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="pw/password_reset_complete.html"), name="password_reset_complete"),

    path("perfil/", editar_perfil, name="editar_perfil"),
    #path("editarperfil/", ProfileUpdate.as_view(), name="editar_perfil_usuario"),


    path('j/<int:id>/', juego, name="juego"),
    path('mantenedor/', mantenedor_juegos, name="mantenedor_juegos"),
    path('mantenedor/agregar_juego/', agregar_juego, name="agregar_juego"),
    path('mantenedor/listado_juegos/', modificar_juego_lista, name="modificar_juego_lista"),
    path('mantenedor/listado_juegos/u/<int:idjuego>/', modificar_juego, name="modificar_juego"),
    path('mantenedor/listado_juegos/d/<idjuego>/', eliminar_juego, name="eliminar_juego"),
    











    







]
