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

from empresa.models import usuario,personalOperativo, detallePerfilOp, vehiculo, mobil, candado, armamento, servicio
from empresa.serializers import UsuarioSerializer, vehiculosSerializer, PersonalOperativoSerializer, candadosSerializer,MobilSerializer, armamentosSerializer, ServicioSerializer

import json

#API VIEW para obtener los servicios creados por los administradores
@api_view(['GET', 'POST'])
@csrf_exempt
def obtenerServicio(request):
    if request.method == 'GET':
        servicios = servicio.objects.all()

        nombre_Servicio = request.GET.get('nombreServicio', None)
        if nombre_Servicio is not None:
            servicios = servicios.filter(nombre_Servicio_icontains=nombre_Servicio)

        servicios_serializer = ServicioSerializer(servicios, many=True)
        return JsonResponse(servicios_serializer.data, safe=False)


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


@api_view(['GET','POST'])
@csrf_exempt
def crearPersonal(request):
    if request.method == 'POST':
        personalRegistrar_Data = JSONParser().parse(request)
        personalRegistrar_Serializer = PersonalOperativoSerializer(data = personalRegistrar_Data)
        if personalRegistrar_Serializer.is_valid():
            personalRegistrar_Serializer.save()
            return JsonResponse(personalRegistrar_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(personalRegistrar_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        personalOp = personalOperativo.objects.all()
        
        nombre = request.GET.get('nombres', None)
        if nombre is not None:
            personalOp = personalOp.filter(nombre_icontains=nombre)
        personalOp_serializer = PersonalOperativoSerializer(personalOp, many=True)
        return JsonResponse(personalOp_serializer.data, safe=False)

@api_view(['GET'])
@csrf_exempt
def obtenerPersonal(request):
    if request.method == 'GET':
        _personalOp = list(personalOperativo.objects.values())
        serializer = PersonalOperativoSerializer(_personalOp, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@csrf_exempt
def agregarPersonal(request):
    if request.method == 'GET':
        _personalOp = list(personalOperativo.objects.values())
        serializer = PersonalOperativoSerializer(_personalOp, many=True)
        return JsonResponse(serializer.data, safe=False)

#Para el personal Operativo
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def personalApi(request,id=0):
    '''
    #registrar un nuevo usuario
    if request.method == 'POST':
        
    elif request.method == 'GET':
        usuarios = usuario.objects.all()
        
        nombre = request.GET.get('nombres', None)
        if nombre is not None:
            usuarios = usuarios.filter(nombre_icontains=nombre)
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)

    '''
    if request.method=='GET':
        _personalOp = list(personalOperativo.objects.values())
        serializer = PersonalOperativoSerializer(_personalOp, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method=='POST':
        personalARegistrar_Data = JSONParser().parse(request)
        personalOpARegistrar_Serializer = PersonalOperativoSerializer(data = personalARegistrar_Data)
        if personalOpARegistrar_Serializer.is_valid():
            personalOpARegistrar_Serializer.save()
            return JsonResponse(personalOpARegistrar_Serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(personalOpARegistrar_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    elif request.method=='PUT':
        personalOp_data = json.loads(request.body)
        _personalOp = list(personalOperativo.filter(id=id).objects.values())
        serializer=PersonalOperativoSerializer(employee,data=personalOp_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        _personalOp = list(personalOperativo.objectsfilter(id=id).values())
        if len(_personalOp) > 0:
            personalOperativo.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse("Deleted Succeffully!!", safe=False)

#inventario Vehiculo
@api_view(['GET'])
@csrf_exempt
def obtenerVehiculo(request):
    if request.method == 'GET':
        _vehiculos = list(vehiculo.objects.values())
        serializer = vehiculosSerializer(_vehiculos, many=True) 
        return JsonResponse(serializer.data, safe=False)

#inventario candado
@api_view(['GET'])
@csrf_exempt
def obtenerCandado(request):
    if request.method == 'GET':
        _candados = list(candado.objects.values())
        serializer = candadosSerializer(_candados, many=True)
        return JsonResponse(serializer.data, safe=False)

#inventario armamento
@api_view(['GET'])
@csrf_exempt
def obtenerArmamento(request):
    if request.method == 'GET':
        _armamentos = list(armamento.objects.values())
        serializer = armamentosSerializer(_armamentos, many=True)
        return JsonResponse(serializer.data, safe=False)

#inventario mobil
@api_view(['GET'])
@csrf_exempt
def obtenerMobil(request):
    if request.method == 'GET':
        _mobil = list(mobil.objects.values())
        serializer = MobilSerializer(_mobil, many=True)
        return JsonResponse(serializer.data, safe=False)


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
        usuarioAppMobil = mobil.objects.get(usuarioApp=UsuarioApp)

        #mandar datos para validación
        if request.method == 'GET':
            usuarioAppMobil_serializer = MobilSerializer(usuarioAppMobil) #El del final es el modelo
            request.session["USER_LOGGED"] = usuarioAppMobil_serializer.data
            return JsonResponse(usuarioAppMobil_serializer.data)
            
        elif request.method == 'PUT':
            usuarioAppMobil_data = JSONParser().parse(request)
            usuarioAppMobil_serializer = MobilSerializer(usuarioAppMobil, data=usuarioAppMobil_data)
            if usuarioAppMobil_serializer.is_valid():
                usuarioAppMobil_serializer.save()


                return JsonResponse(usuarioAppMobil_serializer.data)
                
            return JsonResponse(usuarioAppMobil_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except usuario.DoesNotExist:
        return JsonResponse({'message' : 'El usuario no existe'}, status=status.HTTP_404_NOT_FOUND)

