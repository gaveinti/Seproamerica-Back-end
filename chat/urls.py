from django.urls import path,re_path

from .views import (

    verificar_usuario_receptor_y_crear_canal,
)

UUID_CANAL_REGEX=r'canal/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'
urlpatterns=[
    #re_path(UUID_CANAL_REGEX,CanalDetailView.as_view()),
    re_path(r'^api/chat/(?P<correoU>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', verificar_usuario_receptor_y_crear_canal),

]