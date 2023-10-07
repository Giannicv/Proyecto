from django.shortcuts import render, redirect
from.models import Alumno
# Create your views here.
alumnos= Alumno.objects.all()
def home(request):
    alumnos = Alumno.objects.all()
    return render(request, "gestionCursos.html", {"alumnos": alumnos})


def registrarAlumno(request):
    if request.method == 'POST':
        # Obtén los datos del formulario directamente de la solicitud POST
        codigo = request.POST.get('textCodigo')
        nombre = request.POST.get('textNombre')
        nota = request.POST.get('numNota')

        # Valida los datos si es necesario
        if codigo and nombre and nota:
            # Crea un nuevo alumno y guárdalo en la base de datos
            Alumno.objects.create(codigo=codigo, nombre=nombre, nota=nota)
            return redirect('/')

    # Renderiza el formulario de registro en cualquier caso
    return render(request, "formulario_registro.html")

def eliminarAlumno(request, codigo):
    estudiante = Alumno.objects.get(codigo=codigo)
    estudiante.delete()
    return redirect('/')


