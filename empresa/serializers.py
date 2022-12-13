from rest_framework import serializers 
from empresa.models import usuario 
from empresa.models import vehiculo, mobil, armamento, candado, personalOperativo, personalAdministrativo, pedido, cliente

class UsuarioSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = usuario
        fields = ('sexo_CHOICES',
                  'cedula',
                  'apellidos',
                  'nombres',
                  'fechaNac',
                  'direccion',
                  'telefono',
                  'correo',
                  'contrasenia',
                  'fechaRegistro',
                  'rol')

#Para el inventario
class vehiculosSerializer (serializers.ModelSerializer):
    class Meta:
        model = vehiculo
        fields = (
                'placa',
                'marca',
                'modelo',
                'color',
                'anio')

class candadosSerializer (serializers.ModelSerializer):
    class Meta:
        model = candado
        fields = (
                'numSerie',
                'marca',
                'modelo',
                'color',
                'anio')

class armamentosSerializer (serializers.ModelSerializer):
    class Meta:
        model = armamento
        fields = (
                'numSerie',
                'marca',
                'clase')

class PersonalAdministrativoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = personalAdministrativo
        fields = ('idPersonal',
                  'inicioOperanciones',
                  'finOpeaciones',
                  'sucursal',
                  'cedula',
                  'cargo',
                  'estado',
                  'fechaModificacion',
                  #'rol' 
                  )

class PersonalOperativoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = personalOperativo
        fields = ('sexo_CHOICES',
                  'idPersonal',
                  'numCedula',
                  'apellidos',
                  'nombres',
                  'fechaNac',
                  'sexo',
                  'direccion',
                  'telefono',
                  'correo',
                  'fechaRegistro',
                  #'agregadoPor',
                  #'sucursal',
                  #'estado',
                  #'rol'
                  )

class MobilSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = mobil
        fields = ('numeroCell',
                  'idEquipamiento',
                  'marca',
                  'color',
                  'usuarioApp',
                  'contrasenia',
                  )

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = pedido
        fields = ('idPedido',
                  'nombre_Servicio'
                  'fecha_Solicitud'
                  'fecha_Inicio'
                  'fecha_Finalizacion'
                  'hora_Inicio'
                  'hora_Finalizacion'
                  'cantidad_Empleados_Asignados'
                  'costo'
                  'latitud_Origen'
                  'longitud_Origen'
                  'latitud_Destino'
                  'longitud_Destino'
                )

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = cliente
        fields = ('idCliente',
                  'cedula'
                )