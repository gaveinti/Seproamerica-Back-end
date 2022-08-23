from rest_framework import serializers 
from clienteWA.models import ClienteRegistro
 
 
class ClienteRegistroSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ClienteRegistro
        fields = ('apellidos',
                  'nombres',
                  'cedula',
                  'fNacimiento',
                  'sexo',
                  'correo',
                  'telefono',
                  'contrasenha')