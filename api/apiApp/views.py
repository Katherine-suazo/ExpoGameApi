from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Juego
from .serializers import TodoSerializers

class TodoListApiView(APIView):  # esta es la clase que llamamos en urls, y asi llamar a todos los def

    # permission_classes = [permissions.IsAuthenticated]

    # cualquiera que tenga el endpoint tiene acceso

    def get(self, request, *args, **kwargs):
        todos = Juego.objects.all()
        serializer = TodoSerializers(todos, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):
        data = {
            'nombre': request.data.get('nombre'),
            'año': request.data.get('año'),
            'genero': request.data.get('genero'),
            'user': request.data.get('user')
        }
        serializer = TodoSerializers(data = data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)