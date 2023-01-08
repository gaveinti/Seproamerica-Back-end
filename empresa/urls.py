from django.urls import path, include, re_path
from empresa import views

urlpatterns = [ 
    re_path(r'^api/usuarioInicioSesion$', views.usuarioInicioSesion),
    re_path(r'^api/usuarioInicioSesion/(?P<correoU>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.usuarioInicioSesion),
    re_path(r'^api/usuarioRegistro$', views.usuarioRegistro),
    
    re_path(r'^api/clienteRegistro$', views.clienteRegistro),
    re_path(r'^api/obtenerCliente/(?P<cedula_Cliente>[0-9]+)/$', views.obtenerCliente),
    re_path(r'^api/servicio_seleccionar_actualizar_eliminar/(?P<nombre_Servicio>[a-zA-Z_]+)/$', views.servicio_seleccionar_actualizar_eliminar),

    

    re_path(r'^api/obtenerServicio$', views.obtenerServicio),
    re_path(r'^api/solicitarServicio$', views.solicitarServicio),

  
    #url(r'^api/usuarioRegistro$', views.usuario_Registro_Datos)
    re_path(r'^api/personalAdminRegistro$', views.adminRegistro),
    re_path(r'^api/obtenerAdministrador/(?P<cedula_Admin>[0-9]+)/$', views.obtenerAdministrador),

    re_path(r'^api/personalOperativoRegistro$', views.personalOpRegistro),


    re_path(r'api/visualizarPersonal/', views.personalApi),
    re_path(r'api/visualizarPersonal/[0-9]+',views.personalApi),
    re_path(r'api/visualizarVehiculos/^[a-zA-Z0-9-]+$',views.vehiculoEspecifico),
    re_path(r'api/visualizarVehiculos/',views.obtenerVehiculo),
    re_path(r'api/visualizarCandados/',views.obtenerCandado),
    re_path(r'api/visualizarArmamentos/',views.obtenerArmamento),
    re_path(r'api/visualizarMobil/',views.obtenerMobil),
    re_path(r'api/visualizarSucursales/',views.obtenerSucursal),
    re_path(r'api/visualizarTiposServicios/',views.obtenerTiposServicios),
    re_path(r'^api/crearServicio$',views.crearServicio),



 


    re_path(r'^api/mobilRegistro$', views.mobilRegistro),
    re_path(r'^api/mobilInicioSesion$', views.mobilInicioSesion),
    re_path(r'^api/mobilInicioSesion/(?P<UsuarioApp>\w+)/$', views.mobilInicioSesion),
    ]
