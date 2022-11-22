from django.urls import path,re_path

from .views import (
    #get_all_mensajes,
    verificar_y_crear_canal,
    obtener_canales_usuario_actual,
    obtener_mensajes,
    obtener_mensajes_pr
    )

UUID_CANAL_REGEX=r'canal/(?P<pk>[a-f0 -9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'
urlpatterns=[
    path("api/chat/<str:servicio>/<str:usuario_receptor>/<str:usuario_actual>/",verificar_y_crear_canal),
    #path("api/chat/",get_all_mensajes),
    path("api/chat/inbox/<str:usuario_actual>/",obtener_canales_usuario_actual),
    path("mensajes",obtener_mensajes),
    path("prueba",obtener_mensajes_pr),
    
    
]