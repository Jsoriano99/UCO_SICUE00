from django.db import models
from .choices import UNIVERSIDADES

# Clase base: Usuario
class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        abstract = True  # Usuario es una clase abstracta

# Clase Alumno (hereda de Usuario)
class Alumno(Usuario):
    matricula = models.CharField(max_length=20)
    carrera = models.CharField(max_length=100)
    promedio = models.FloatField()
    creditosSuperados = models.IntegerField()
    creditosRestantes = models.IntegerField()

# Clase Profesor (hereda de Usuario)
class Profesor(Usuario):
    departamento = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

# Clase Administrador (hereda de Usuario)
class Administrador(Usuario):
    rol = models.CharField(max_length=50, default="Coordinador")


# Clase Universidad
class Universidad(models.Model):
    idUniversidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    programas = models.TextField()  # Lista de programas ofrecidos

# Clase Asignatura
class Asignatura(models.Model):
    idAsignatura = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    creditos = models.IntegerField()
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE, related_name='asignaturas')


class Solicitud(models.Model):
    solicitante = models.ForeignKey(
        Alumno, 
        on_delete=models.CASCADE, 
        related_name="solicitudes"
    )  # Relación con Alumno
    universidad_origen = models.CharField(
        max_length=100,
        choices=UNIVERSIDADES,
        default='UCO'
    )
    universidad_destino = models.CharField(
        max_length=100,
        choices=UNIVERSIDADES,
        default='UCO'
    )
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(default='2024-12-31')
    motivo = models.TextField()

    def __str__(self):
        return f"{self.universidad_origen} -> {self.universidad_destino}"


