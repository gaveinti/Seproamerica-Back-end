from django.urls import path

from .views import obtener_notificaciones_por_usuario,obtener_no_leido,marcar_como_leido,guardarTokenMovil

urlpatterns=[
    path("api/notificacion/all/<str:usuario_actual>/",obtener_notificaciones_por_usuario),
    path("api/notificacion/no_leido/<str:usuario_actual>/",obtener_no_leido),
    path("api/notificacion/marcar_como_leido/<int:id>/",marcar_como_leido),

    path("api/notificacion/add_token/",guardarTokenMovil)

    
]
