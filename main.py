import os
import django

# Configuración para usar Django fuera de manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sicue_project.settings')
django.setup()

from sicue.models import Alumno, Profesor, Administrador, Universidad, Solicitud
from sicue.services import (
    crear_solicitud_alumno,
    aceptar_solicitud,
    rechazar_solicitud,
    ver_solicitudes_pendientes,
    asignar_profesor,
    modificar_solicitud,
    ver_solicitudes_por_alumno,
    validar_estado_solicitud
)

# Función para limpiar datos existentes (opcional)
def limpiar_datos():
    Solicitud.objects.all().delete()
    Alumno.objects.all().delete()
    Profesor.objects.all().delete()
    Administrador.objects.all().delete()
    Universidad.objects.all().delete()

# Crear datos de prueba
def crear_datos():
    # Crear universidades
    uco = Universidad.objects.create(nombre="Universidad de Córdoba", ubicacion="Córdoba", programas="Ingeniería, Derecho")
    use = Universidad.objects.create(nombre="Universidad de Sevilla", ubicacion="Sevilla", programas="Arquitectura, Medicina")

    # Crear alumnos
    alumno1 = Alumno.objects.create(
        nombre="Juan", apellidos="Pérez", email="juan@gmail.com", password="1234",
        matricula="A12345", carrera="Ingeniería Informática", promedio=8.5, creditosSuperados=180, creditosRestantes=60
    )
    alumno2 = Alumno.objects.create(
        nombre="Ana", apellidos="García", email="ana@gmail.com", password="1234",
        matricula="B67890", carrera="Derecho", promedio=9.0, creditosSuperados=200, creditosRestantes=30
    )

    # Crear profesores
    profesor1 = Profesor.objects.create(
        nombre="Luis", apellidos="Martínez", email="luis@gmail.com", password="1234",
        departamento="Matemáticas", especialidad="Cálculo"
    )
    profesor2 = Profesor.objects.create(
        nombre="Marta", apellidos="Fernández", email="marta@gmail.com", password="1234",
        departamento="Derecho", especialidad="Procesal"
    )

    # Crear administradores
    admin = Administrador.objects.create(
        nombre="Carlos", apellidos="Gómez", email="carlos@gmail.com", password="1234", rol="Coordinador SICUE"
    )
    admin2 = Administrador.objects.create(
        nombre="Jorge", apellidos="Soriano", email="jsoriano00@gmail.com", password="4567", rol="Coordinador SICUE"
    )

    return uco, use, alumno1, alumno2, profesor1, profesor2, admin, admin2

# Probar funcionalidades
def main():
    # Limpiar datos existentes
    limpiar_datos()

    # Crear datos iniciales
    uco, use, alumno1, alumno2, profesor1, profesor2, admin, admin2 = crear_datos()

    # Crear solicitudes
    solicitud1 = crear_solicitud_alumno(alumno1, "Pendiente", uco, use)
    solicitud2 = crear_solicitud_alumno(alumno2, "Pendiente", use, uco)

    # Ver solicitudes pendientes
    pendientes = ver_solicitudes_pendientes()
    print("Solicitudes pendientes:")
    for solicitud in pendientes:
        print(f" - Solicitud {solicitud.idSolicitud} de {solicitud.estudiante.nombre} ({solicitud.estado})")

    # Aceptar una solicitud
    solicitud1 = aceptar_solicitud(solicitud1)
    print(f"Solicitud {solicitud1.idSolicitud} aceptada.")

    # Rechazar una solicitud
    solicitud2 = rechazar_solicitud(solicitud2)
    print(f"Solicitud {solicitud2.idSolicitud} rechazada.")

    # Asignar un profesor a la solicitud aceptada
    solicitud1 = asignar_profesor(solicitud1, profesor1)
    print(f"Profesor {profesor1.nombre} asignado a la solicitud {solicitud1.idSolicitud}.")

    # Ver solicitudes por alumno
    solicitudes_alumno1 = ver_solicitudes_por_alumno(alumno1)
    print(f"Solicitudes de {alumno1.nombre}:")
    for solicitud in solicitudes_alumno1:
        print(f" - Solicitud {solicitud.idSolicitud} ({solicitud.estado})")

    # Modificar solicitud
    print(f"Modificando la solicitud {solicitud1.idSolicitud}...")
    modificar_solicitud(solicitud1, {"estado": "En proceso", "profesor": profesor2})
    print(f"Solicitud {solicitud1.idSolicitud} modificada. Estado: {solicitud1.estado}, Profesor: {solicitud1.profesor.nombre}")

    # Validar estado antes de intentar otra acción
    try:
        validar_estado_solicitud(solicitud1, ["Pendiente"])
        rechazar_solicitud(solicitud1)
    except ValueError as e:
        print(f"Error al intentar rechazar la solicitud: {e}")

    # Cambiar estado y validar nuevamente
    modificar_solicitud(solicitud1, {"estado": "Pendiente"})
    rechazar_solicitud(solicitud1)
    print(f"Solicitud {solicitud1.idSolicitud} rechazada tras corregir estado.")

if __name__ == "__main__":
    main()