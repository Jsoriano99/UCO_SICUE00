from .models import Alumno, Profesor, Administrador, Solicitud, Universidad

def crear_solicitud_alumno(alumno, estado, universidad_origen, universidad_destino):
    """
    Crea una solicitud para un alumno.
    """
    solicitud = Solicitud(
        estado=estado,
        estudiante=alumno,
        universidadOrigen=universidad_origen,
        universidadDestino=universidad_destino,
    )
    solicitud.save()
    return solicitud

def aceptar_solicitud(solicitud):
    """
    Cambia el estado de una solicitud a 'Aprobada'.
    """
    solicitud.estado = "Aprobada"
    solicitud.save()
    return solicitud

def rechazar_solicitud(solicitud):
    """
    Cambia el estado de una solicitud a 'Rechazada'.
    """
    solicitud.estado = "Rechazada"
    solicitud.save()
    return solicitud

# Listar todas las solicitudes pendientes
def ver_solicitudes_pendientes():
    return Solicitud.objects.filter(estado="Pendiente")

# Asignar un profesor a una solicitud
def asignar_profesor(solicitud, profesor):
    solicitud.profesor = profesor
    solicitud.save()
    return solicitud

def modificar_solicitud(solicitud, nuevos_datos):
    for key, value in nuevos_datos.items():
        if hasattr(solicitud, key):
            setattr(solicitud, key, value)
    solicitud.save()
    return solicitud

def ver_solicitudes_por_alumno(alumno):
    return alumno.solicitudes.all()

def validar_estado_solicitud(solicitud, estados_permitidos):
    if solicitud.estado not in estados_permitidos:
        raise ValueError(f"Estado '{solicitud.estado}' no permitido. Estados permitidos: {estados_permitidos}")
    return True