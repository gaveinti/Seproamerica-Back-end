from django.conf.urls import url
from clienteWA import views 
 
urlpatterns = [ 
    url(r'^usuarioInicioSesion/$', views.clienteInicioSesionApi)
    #url(r'^api/usuarioRegistro$', views.usuario_Registro_Datos)

]