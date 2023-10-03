from django.shortcuts import render
from.models import Alumno
# Create your views here.
alumnos= Alumno.objects.all()
def home(request):
    return render(request, "gestionCursos.html", {"alumnos": alumnos})