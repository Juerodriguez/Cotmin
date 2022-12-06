from django import forms


class ConsultForm(forms.Form):
    number = forms.CharField(label="N° de Expediente", max_length=200)
    tipo = forms.CharField(label="Tipo de tramite", max_length=200)
