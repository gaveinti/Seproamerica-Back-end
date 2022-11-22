from django.urls import path, include, re_path
from empresa import views

urlpatterns = [ 
    re_path(r'^api/usuarioInicioSesion$', views.usuarioInicioSesion),
    re_path(r'^api/usuarioInicioSesion/(?P<correoU>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.usuarioInicioSesion),
    re_path(r'^api/usuarioRegistro$', views.usuarioRegistro),
    #url(r'^api/usuarioRegistro$', views.usuario_Registro_Datos)

    re_path(r'^api/mobilRegistro$', views.mobilRegistro),
    re_path(r'^api/mobilInicioSesion$', views.mobilInicioSesion),
    re_path(r'^api/mobilInicioSesion/(?P<UsuarioApp>\w+)/$', views.mobilInicioSesion),
]