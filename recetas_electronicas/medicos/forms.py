from django import forms

class MedicoForm(forms.Form):
    apellido = forms.CharField(max_length=15, required=True)
    nombre = forms.CharField(max_length=15, required=True)
    matricula = forms.IntegerField(required=True)
    profesion = forms.CharField(max_length=15, required=True)
    usuario = forms.CharField(max_length=15, required=True)
    contraseña = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=False)
    sector = forms.CharField(max_length=15, required=True)

class PersonalFrom(forms.Form):
    apellido = forms.CharField(max_length=15, required=True)
    nombre = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=False)
    sector = forms.CharField(max_length=15, required=True)

class TurnosForm(forms.Form):
    especialidad = forms.CharField(max_length=15, required=True)
    turno = forms.DateField(required=True)