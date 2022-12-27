from django.urls import path,re_path

from .views import (
    #get_all_mensajes,
    verificar_y_crear_canal,
    obtener_canales_usuario_actual,
    )

#UUID_CANAL_REGEX=r'canal/(?P<pk>[a-f0 -9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'
urlpatterns=[
    path("api/chat/<str:id_servicio>/<str:servicio>/<str:usuario_receptor>/<str:usuario_actual>/",verificar_y_crear_canal),
    path("api/chat/inbox/<str:usuario_actual>/",obtener_canales_usuario_actual),
    
    
]