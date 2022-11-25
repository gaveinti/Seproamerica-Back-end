from rest_framework import serializers 
from empresa.models import usuario 
from empresa.models import personalOperativo
 
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

class PersonalOperativoSerializer (serializers.ModelSerializer):
    class Meta:
        model = personalOperativo
        fields = (
                'idPersonal',
                'numCedula',
                'apellidos',
                'nombres',
                'fechaNac',
                'sexo',
                'direccion',
                'telefono',
                'correo',
                'fechaRegistro')
                #'sucursal',
                #'estado')

'''
class MobilSerializer(serializers.ModelSerializer):
    class Meta:
        model = mobil
        fields = ('numeroCell',
                'idEquipamiento',
                'marca',
                'color')      
'''

