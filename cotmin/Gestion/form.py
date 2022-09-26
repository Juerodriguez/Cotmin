from django import forms
from .models import Tramites


class TramiteForm(forms.ModelForm):
    class Meta:
        model = Tramites
        fields = ['number', 'tipo', 'solicitante', 'nota_by_admin']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control',
                                               'placeholder': 'Escribe numero del expediente'}),
            'solicitante': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Nombre del responsable'}),
            'nota_by_admin': forms.Textarea(attrs={'class': 'form-control',
                                               'placeholder': 'Espacio para notas'}),
        }




