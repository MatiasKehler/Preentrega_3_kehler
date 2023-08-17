from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, "medicos/home.html")

def medicos(request):
    prueba = {'doctor': Medicos.objects.all() }
    return render(request, "medicos/medicos.html", prueba)

def personal(request):
    test = {'personas': Personal.objects.all()}
    return render(request, "medicos/personal.html", test)

def turnos(request):
    test1 = {'fechas': Turnos.objects.all()}
    return render(request, "medicos/turnos.html", test1)

def add_medico(request):
    if request.method == "POST":
        formulario = MedicoForm(request.POST)
        if formulario.is_valid():
            formulario_apellido = formulario.cleaned_data.get('apellido')
            formulario_nombre = formulario.cleaned_data.get('nombre')
            formulario_matricula = formulario.cleaned_data.get('matricula')
            formulario_profesion = formulario.cleaned_data.get('profesion')
            formulario_usuario = formulario.cleaned_data.get('usuario')
            formulario_contraseña = formulario.cleaned_data.get('contraseña')
            formulario_email = formulario.cleaned_data.get('email')
            formulario_sector = formulario.cleaned_data.get('sector')
            final = Medicos(apellido = formulario_apellido, nombre = formulario_nombre, matricula = formulario_matricula,
                            profesion = formulario_profesion, usuario = formulario_usuario, contraseña = formulario_contraseña,
                            email = formulario_email, sector = formulario_sector)
            final.save()
            return render(request, "medicos/home.html")
    else:
        formulario = MedicoForm()

    return render(request, "medicos/agregar_medico.html", {"form": formulario})

def add_personal(request):
    if request.method == "POST":
        formulario = PersonalFrom(request.POST)
        if formulario.is_valid():
            formulario_apellido = formulario.cleaned_data.get('apellido')
            formulario_nombre = formulario.cleaned_data.get('nombre')
            formulario_email = formulario.cleaned_data.get('email')
            formulario_sector = formulario.cleaned_data.get('sector')
            final = Personal(apellido = formulario_apellido, nombre = formulario_nombre,
                            email = formulario_email, sector = formulario_sector)
            final.save()
            return render(request, "medicos/home.html")
    else:
        formulario = PersonalFrom()

    return render(request, "medicos/agregar_personal.html", {"form": formulario})

def add_turno(request):
    if request.method == "POST":
        formulario = TurnosForm(request.POST)
        if formulario.is_valid():
            formulario_especialidad = formulario.cleaned_data.get('especialidad')
            formulario_turno = formulario.cleaned_data.get('turno')
            final = Turnos(especialidad = formulario_especialidad, turno = formulario_turno)
            final.save()
            return render(request, "medicos/home.html")
    else:
        formulario = TurnosForm()

    return render(request, "medicos/agregar_turno.html", {"form": formulario})

def buscarmedicos(request):
    return render(request, "medicos/buscar_medico.html")

def buscar2(request):
    if request.GET['buscar']:
        busqueda = request.GET['buscar']
        apellido = Medicos.objects.filter(apellido__icontains = busqueda)
        nombre = Medicos.objects.filter(nombre__icontains= busqueda)
        if nombre:
            context = {'doctor': nombre}
        if apellido:
            context = {'doctor': apellido}
        return render(request, "medicos/medicos.html", context)
    return HttpResponse("Ingreso un dato no valido.")
