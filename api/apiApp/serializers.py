from rest_framework import serializers
from .models import Juego


class TodoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Juego
        fields = ['nombre', 'año', 'genero', 'user']


        