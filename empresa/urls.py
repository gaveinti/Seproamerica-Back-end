from django.urls import path, include, re_path
from empresa import views

urlpatterns = [ 
    re_path(r'^api/usuarioRegistro$', views.usuarioRegistro),
    
    #url(r'^api/usuarioRegistro$', views.usuario_Registro_Datos)
]