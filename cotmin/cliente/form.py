from django import forms
from gestion.models import Tramites


class ConsultForm(forms.ModelForm):
    class Meta:
        model = Tramites
        fields = ['number', 'tipo']
