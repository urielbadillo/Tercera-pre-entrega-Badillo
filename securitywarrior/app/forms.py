from django import forms


class Appliance_Forms(forms.Form):
    compania = forms.CharField(max_length=50, required=True)
    costo = forms.IntegerField(required=True)
    licencia = forms.CharField(max_length=50, required=True)


class Cursos_Forms(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    costo = forms.IntegerField(required=True)
    tiempo = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(max_length=50, required=True)


class Servicios_Forms(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    costo = forms.IntegerField(required=True)
    caracteristicas = forms.CharField(max_length=50, required=True)


class Eventos_Forms(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    fecha = forms.DateTimeField(required=True)
    costo = forms.IntegerField(required=True)
    lugar = forms.CharField(max_length=50, required=True)
