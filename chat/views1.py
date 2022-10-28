from empresa.serializers import UsuarioSerializer
from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import CanalMensaje,CanalUsuario,Canal
from django.http import HttpResponse,Http404,JsonResponse


from django.views.generic.edit import FormMixin

from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view

from empresa import views, models

# Create your views here.

def verificar_usuario_receptor_y_crear_canal(request,correoU):
    try:
        usuarioAEncontrar = models.usuario.objects.get(correo=correoU)
        #mandar datos para validación
        if request.method == 'GET':
            correo_usuario_receptor=usuarioAEncontrar.correo
            correo_usuario_actual=JsonResponse(request.session.get('USER_LOGGED'))
            print(correo_usuario_receptor,correo_usuario_receptor)
            return HttpResponse({'res':correo_usuario_receptor,'resq':correo_usuario_actual})
            

    except models.usuario.DoesNotExist:
                return HttpResponse("No existe usuario receptor")




class CanalDetailView(LoginRequiredMixin,DetailView):
    #template_name: 'directMessage/canal_detail.html'
    
    queryset = Canal.objects.all()

    def get_content_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        obj = context['object']
        print(obj)

        #if self.request.user not in obj.usuarios.all():
        #    raise PermissionDenied
        context['si_canal_miembro']=self.request.user in obj.usuarios.all()
        return context

    '''
    def get_queryset(self):
        usuario= self.request.user
        username= usuario.username
        qs= Canal.objects.all().filtrar_por_username(username)
        return qs
    '''




class DetailMs(LoginRequiredMixin,DetailView):
    def  get_object(self,*args,**kwargs):
        
        username= self.kwargs.get("username")
        mi_username=self.request.user.username
        
        if username == mi_username:
            mi_canal,_=Canal.objects.obtener_o_crear_canal_usuario_actual(self.request.user)
            return JsonResponse( {'canal':mi_canal.id})
        canal,_= Canal.objects.obtener_o_crear_canal_ms(mi_username,username)

        if canal == None:
            raise Http404
        

        return JsonResponse(canal)





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









def mensajes_privados(request,username,*args,**kwargs):

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




@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def get_all_mensajes(request):
    if request.method == 'GET':
        mensajes= Canal.objects.all()
        render(mensajes)



def prueba(request,username,*args,**kwargs):
    print(kwargs.get("username"))
    u=kwargs.get("username")

    return HttpResponse(f"Canal con usuario - {u }")
