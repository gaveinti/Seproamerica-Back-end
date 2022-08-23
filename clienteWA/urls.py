from django.conf.urls import url
from clienteWA import views 
 
urlpatterns = [ 
    url(r'^api/usuarioInicioSesion$', views.usuario_Inicio_Sesion_Datos),
    url(r'^api/usuarioRegistro$', views.usuario_Registro_Datos)

]