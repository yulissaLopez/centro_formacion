from rest_framework import serializers
from .models import Estudiante, Nota
from rest_framework.exceptions import ValidationError

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ['estudiante', 'calificacion']

class EstudianteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['documento_identidad','nombre', 'apellido', 'promedio_general', 'estado']
        
    def validate_documento_identidad(self, value):
        print("Validando documento_identidad...") 
        if Estudiante.objects.filter(documento_identidad=value).exists():
            raise ValidationError(f"Ya existe un estudiante con el documento de identidad {value}.")
        return value

class EstudianteSerializer(serializers.ModelSerializer):
    notas = NotaSerializer(many=True, read_only=True)
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'promedio_general', 'notas']
