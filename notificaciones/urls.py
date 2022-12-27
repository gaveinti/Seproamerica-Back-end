from django.urls import path

from .views import obtener_notificaciones_por_usuario

urlpatterns=[
    path("api/notificacion/<str:usuario_actual>/",obtener_notificaciones_por_usuario)

]