from django.db import models
from .managers import EstudianteManager

# Create your models here.

class Estudiante(models.Model):

    #Informacion personal
    documento_identidad = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    promedio_general = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    estado = models.CharField(max_length=100, default="Nuevo")
    active = models.BooleanField(default=True)

    objects = EstudianteManager()
    all_objects = models.Manager()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.documento_identidad}"

    def delete(self, *args, **kwargs):
        self.active = False
        self.save()

    # Funcion para calcular el promedio
    def calcular_promedio(self):

        #Obtener las notas a traves del related name del modelo Nota
        notas = self.notas.all()

        if notas.exists():
            promedio_general = sum(nota.calificacion for nota in notas) / len(notas)
            self.promedio_general = promedio_general

            if self.promedio_general >= 3.0:
                self.estado = "Aprobado"
            else:
                self.estado = "No Aprobado"

            self.save()
        else:
            self.promedio_general = 0.0
            self.save()
    
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    

class Nota(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="notas", to_field="documento_identidad")
    calificacion  = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Nota de {self.estudiante.nombre} {self.estudiante.apellido} - {self.calificacion}"