from http.client import HTTPResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
# Para agregar mensaje y verificar la conexion
from django.contrib import messages

from empresa.models import usuario,mobil
from empresa.serializers import UsuarioSerializer, MobilSerializer





# Create your views here.
@api_view(['GET', 'POST'])
@csrf_exempt
def usuarioRegistro(request):
    #registrar un nuevo usuario
    if request.method == 'POST':
        usuarioARegistrar_Data = JSONParser().parse(request)
        usuarioARegistrar_Serializer = UsuarioSerializer(data = usuarioARegistrar_Data)
        if usuarioARegistrar_Serializer.is_valid():
            usuarioARegistrar_Serializer.save()
            return JsonResponse(usuarioARegistrar_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(usuarioARegistrar_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        usuarios = usuario.objects.all()
        
        nombre = request.GET.get('nombres', None)
        if nombre is not None:
            usuarios = usuarios.filter(nombre_icontains=nombre)
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)


#Función para obtener datos de un usuario para validacion en inicio sesion
@api_view(['GET', 'PUT'])
@csrf_exempt
def usuarioInicioSesion(request, correoU):
    #pk = self.kwargs.get('pk')
    #Encontrar usuario por pk (cedula)
    #print(usuario.objects.get())
    try:
        usuarioAEncontrar = usuario.objects.get(correo=correoU)

        #mandar datos para validación
        if request.method == 'GET':
            usuarioAEncontrar_serializer = UsuarioSerializer(usuarioAEncontrar) #El del final es el modelo
            request.session["USER_LOGGED"] = usuarioAEncontrar_serializer.data
            return JsonResponse(usuarioAEncontrar_serializer.data)
        elif request.method == 'PUT':
            usuarioAEncontrar_data = JSONParser().parse(request)
            usuarioAEncontrar_serializer = UsuarioSerializer(usuarioAEncontrar, data=usuarioAEncontrar_data)
            if usuarioAEncontrar_serializer.is_valid():
                usuarioAEncontrar_serializer.save()


                return JsonResponse(usuarioAEncontrar_serializer.data)
                
            return JsonResponse(usuarioAEncontrar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except usuario.DoesNotExist:
        return JsonResponse({'message' : 'El usuario no existe'}, status=status.HTTP_404_NOT_FOUND)




def mobilRegistro(request):
    #registrar un nuevo usuario

    if request.method == 'GET':
        mobils = mobil.objects.all()
        
        numeroCell = request.GET.get('numeroCell', None)
        if numeroCell is not None:
            mobils = mobils.filter(numeroCell_icontains=numeroCell)
        mobils_serializer = MobilSerializer(mobils, many=True)
        return JsonResponse(mobils_serializer.data, safe=False)


        
#Función para obtener datos de un usuario para validacion en inicio sesion
@api_view(['GET', 'PUT'])
@csrf_exempt
def mobilInicioSesion(request, UsuarioApp):

    try:
        usuarioAppMobil = usuario.objects.get(UsuarioApp=UsuarioApp)

        #mandar datos para validación
        if request.method == 'GET':
            usuarioAppMobil_serializer = UsuarioSerializer(usuarioAppMobil) #El del final es el modelo
            request.session["USER_LOGGED"] = usuarioAppMobil_serializer.data
            return JsonResponse(usuarioAppMobil_serializer.data)
            
        elif request.method == 'PUT':
            usuarioAppMobil_data = JSONParser().parse(request)
            usuarioAppMobil_serializer = UsuarioSerializer(usuarioAppMobil, data=usuarioAppMobil_data)
            if usuarioAppMobil_serializer.is_valid():
                usuarioAppMobil_serializer.save()


                return JsonResponse(usuarioAppMobil_serializer.data)
                
            return JsonResponse(usuarioAppMobil_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except usuario.DoesNotExist:
        return JsonResponse({'message' : 'El usuario no existe'}, status=status.HTTP_404_NOT_FOUND)