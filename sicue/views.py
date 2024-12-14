from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from sicue.models import Alumno, Universidad, Solicitud, Profesor, Administrador
from .services import crear_solicitud_alumno
from django.contrib import messages
from .forms import SolicitudForm



class CustomLoginView(LoginView):
    template_name = 'login.html'

def login_view(request):
    if request.method == "POST":
        print("POST recibido")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(f"Email recibido: {email}, Contraseña recibida: {password}")

        # Inicializar variables
        usuario = None
        rol = None

        # Buscar en Alumno
        if Alumno.objects.filter(email=email, password=password).exists():
            usuario = Alumno.objects.get(email=email)
            rol = "alumno"
            print(f"Alumno encontrado: {usuario.nombre} (ID: {usuario.pk})")

        # Buscar en Profesor
        elif Profesor.objects.filter(email=email, password=password).exists():
            usuario = Profesor.objects.get(email=email)
            rol = "profesor"
            print(f"Profesor encontrado: {usuario.nombre} (ID: {usuario.pk})")

        # Buscar en Administrador
        elif Administrador.objects.filter(email=email, password=password).exists():
            usuario = Administrador.objects.get(email=email)
            rol = "administrador"
            print(f"Administrador encontrado: {usuario.nombre} (ID: {usuario.pk})")

        # Si no se encuentra ningún usuario
        if not usuario:
            print("No se encontró ningún usuario con las credenciales proporcionadas.")
            messages.error(request, "Credenciales inválidas. Por favor, inténtalo de nuevo.")
            return render(request, "login.html")

        # Guardar los datos del usuario en la sesión
        print(f"Guardando usuario en sesión: {usuario.email}, Rol: {rol}")
        request.session["usuario_id"] = usuario.pk
        request.session["usuario_email"] = usuario.email
        request.session["usuario_rol"] = rol

        # Redirigir según el rol
        if rol == "alumno":
            return redirect("menu_estudiante")
        elif rol == "profesor":
            return redirect("menu_profesor")
        elif rol == "administrador":
            return redirect("menu_administrador")

    return render(request, "login.html")
   

@login_required
def menu_administrador(request):
    if request.session.get("usuario_rol") != "administrador":
        return redirect("login")
    return render(request, "menu_administrador.html")

@login_required
def menu_estudiante(request):
    if request.session.get("usuario_rol") != "alumno":
        return redirect("login")
    
    alumno = Alumno.objects.get(pk=request.session.get("usuario_id"))
    return render(request, "menu_estudiante.html", {"alumno": alumno})

@login_required
def menu_profesor(request):
    if request.session.get("usuario_rol") != "profesor":
        return redirect("login")
    return render(request, "menu_profesor.html")



@login_required
def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.solicitante = Alumno.objects.get(pk=request.session.get("usuario_id"))  # Relación con Alumno
            solicitud.save()
            return redirect('menu_estudiante')  # Cambia esto por la URL correspondiente
    else:
        form = SolicitudForm()
    return render(request, 'crear_solicitud.html', {'form': form})


@login_required
def listar_solicitudes(request):
    if request.session.get("usuario_rol") != "alumno":
        return redirect("login")

    alumno = Alumno.objects.get(pk=request.session.get("usuario_id"))
    solicitudes = Solicitud.objects.filter(solicitante=alumno)  # Filtra solicitudes del alumno autenticado

    return render(request, "listar_solicitudes.html", {"solicitudes": solicitudes})

