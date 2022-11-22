from rest_framework import serializers 
from chat.models import Mensaje

class MensajeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Mensaje
        fields = ('canal',
                  'usuario'
                  
                  )
