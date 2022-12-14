from rest_framework import serializers 
from clienteWA.models import ClienteInicioSesion, ClienteRegistro
 # Prueba integracion #182724927
 
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

class ClienteInicioSesionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClienteInicioSesion
        fields = (
            'correo',
            'contrasenha'  )
