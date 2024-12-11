from django.db import models

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

# Clase Solicitud
class Solicitud(models.Model):
    idSolicitud = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=20)  # Ej. "Pendiente", "Aprobada"
    estudiante = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='solicitudes')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, blank=True)
    universidadOrigen = models.ForeignKey(Universidad, on_delete=models.CASCADE, related_name='solicitudes_origen')
    universidadDestino = models.ForeignKey(Universidad, on_delete=models.CASCADE, related_name='solicitudes_destino')
