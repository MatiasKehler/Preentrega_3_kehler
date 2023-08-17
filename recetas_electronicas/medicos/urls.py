from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name= "home"),
    path('medicos/', medicos, name= "medicos"),
    path('personal/', personal, name= "personal"),
    path('turnos/', turnos, name= "turnos"),
    path('agregar_medico/', add_medico, name="agregar_medico"),
    path('agregar_personal/', add_personal, name="agregar_personal"),
    path('agregar_turno/', add_turno, name="agregar_turno"),
    path('buscar_medico/', buscarmedicos, name="buscar_medico"),
    path('buscar2', buscar2, name="buscar2"),
]