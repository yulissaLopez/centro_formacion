from django.shortcuts import render
from .models import Estudiante, Nota
from .serializers import EstudianteSerializer, NotaSerializer, EstudianteListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class EstudianteListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteListSerializer

class EstudianteManageView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    lookup_field = 'documento_identidad'

    def get_object(self):
        documento_identidad = self.kwargs['documento_identidad']
        return Estudiante.objects.get(documento_identidad=documento_identidad)

class NotaCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

    #Actualizar el promedio 
    def perform_create(self, serializer):

        #Obtengo el numero del documento del estudiante desde la request
        id = self.request.data.get('estudiante')

        try:
            estudiante = Estudiante.objects.get(documento_identidad = id)
        except Estudiante.DoesNotExist:
            raise NotFound(detail="Estudiante no encontrado.")
        
        serializer.save(estudiante=estudiante)

        estudiante.calcular_promedio()

     

