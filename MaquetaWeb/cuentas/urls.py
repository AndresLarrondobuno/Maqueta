from django.urls import re_path
from .views import *


app_name = 'cuentas'

urlpatterns = [
    re_path(r'^registrarse/$', usuariosController.registrarUsuarioView, name='registrarse'),
    re_path(r'^iniciar_sesion/$', usuariosController.iniciarSesionView, name='iniciarSesion'),
    re_path(r'^cerrar_sesion/$', usuariosController.cerrarSesionView, name='cerrarSesion'),

]