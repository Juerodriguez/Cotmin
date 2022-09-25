from django.forms import ModelForm
from .models import Tramites


class TramiteForm(ModelForm):
    class Meta:
        model = Tramites
        fields = ['number', 'tipo', 'solicitante', 'nota_by_admin']




