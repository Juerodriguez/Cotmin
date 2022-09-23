from django.forms import ModelForm
from .models import Tramites


class TramiteForm(ModelForm):
    class Meta:
        model = Tramites
        fields = ['number', 'tipo', 'estado', 'nota_by_admin']


class ManagerForm(ModelForm):
    class Meta:
        model = Tramites
        fields = []

