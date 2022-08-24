#from django.conf.urls import url
from django.urls import path, include, re_path
from clienteWA import views 
 
urlpatterns = [ 
    re_path(r'^usuarioInicioSesion/$', views.clienteInicioSesionApi)
    #url(r'^api/usuarioRegistro$', views.usuario_Registro_Datos)

]