from django.urls import path
from apps.usuario.views import *

app_name = 'usuario'

urlpatterns = [
    path('listado_usuarios', ListadoUsuario.as_view(), name='listar_usuarios'),
    path('registrar_usuario', RegistarUsuario.as_view(), name='Registrar_usuario'),
    path('editar_usuario/<int:pk>/', EditarUsuario.as_view(), name='editar_usuario'),
    path('eliminar_usuario/<int:pk>/', EliminarUsuario.as_view(), name='eliminar_usuario')
    

]
