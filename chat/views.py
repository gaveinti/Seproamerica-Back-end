from empresa.serializers import UsuarioSerializer
from django.views.generic import DetailView
from django.core.exceptions import PermissionDenied
from .models import CanalMensaje,CanalUsuario,Canal
from django.http import HttpResponse,Http404,JsonResponse


from django.views.generic.edit import FormMixin

from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view

from empresa import views, models


@api_view(['GET', 'POST'])
@csrf_exempt
def verificar_usuario_receptor_y_crear_canal(request,correoU):
    try:
        usuarioAEncontrar = models.usuario.objects.get(correo=correoU)
        #mandar datos para validación
        if request.method == 'GET':
            correo_usuario_receptor=usuarioAEncontrar.correo
            correo_usuario_actual=request.session.get('USER_LOGGED')["correo"]
            print(correo_usuario_actual)
            
            canal,created= Canal.objects.obtener_o_crear_canal_ms_por_correo(correo_usuario_actual,correoU)

            if created:
                print("Frue creado!")
                Usuarios_Canal=canal.canalusuario_set.all().values("usuario__correo")
                print(Usuarios_Canal)
                mensaje_canal=canal.canalmensaje_set.all()
                print(mensaje_canal.values("texto"))

        return JsonResponse({"canal-id":created,'actual':correo_usuario_actual,'receptor':correo_usuario_receptor})
            
            
        #return JsonResponse({'actual':correo_usuario_actual,'receptor':correo_usuario_receptor})
            

    except models.usuario.DoesNotExist:
                return HttpResponse("No existe usuario receptor")



@api_view(['GET', 'POST'])
@csrf_exempt
def crear_canal(request,username):
    
    if request.method == 'GET':
        if not request.user.is_authenticated:
                return HttpResponse("Prohibido")

        #usuario logeado
        mi_username = request.user.username
        
        canal,created= Canal.objects.obtener_o_crear_canal_ms(mi_username,username)
        if created:
            print("Frue creado!")
        Usuarios_Canal=canal.canalusuario_set.all().values("usuario__username")
        print(Usuarios_Canal)
        mensaje_canal=canal.canalmensaje_set.all()
        print(mensaje_canal.values("texto"))

        return JsonResponse({"canal-id":canal.id})
        #return HttpResponse(f"Nuestro ID del  Canal - {canal.id}")

        