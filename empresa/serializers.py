from rest_framework import serializers 
from empresa.models import usuario, personalAdministrativo, personalOperativo 
class UsuarioSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = usuario
        fields = ('sexo_CHOICES',
                  'cedula',
                  'apellidos',
                  'nombres',
                  'fechaNac',
                  'sexo',
                  'direccion',
                  'telefono',
                  'correo',
                  'contrasenia',
                  'fechaRegistro',
                  'rol')

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
                  'agregadoPor',
                  'sucursal',
                  'estado',
                  #'rol'
                  )