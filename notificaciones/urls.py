from django.urls import path

from .views import obtener_notificaciones_por_usuario,obtener_no_leido,marcar_como_leido,guardar_token_movil,obtener_tokens,notificar_FCM,notificar,notificar_administradores,obtener_token,notificar_individual_FCM

urlpatterns=[
    path("api/notificacion/all/<str:usuario_actual>/",obtener_notificaciones_por_usuario),
    path("api/notificacion/no_leido/<str:usuario_actual>/",obtener_no_leido),
    path("api/notificacion/marcar_como_leido/<int:id>/",marcar_como_leido),

    path("api/notificacion/add_token/",guardar_token_movil),
    path("api/notificacion/all_token/",obtener_tokens),
    path("api/notificacion/get_token/<str:cedula>/",obtener_token),
    path("api/notificacion/notificar_all_fcm_movil/",notificar_FCM),
    path("api/notificacion/notificar_fcm_movil/",notificar_individual_FCM),
    path("api/notificacion/notificar/",notificar),
    path("api/notificacion/notificar_admin/",notificar_administradores)
    
    
    

    
]
