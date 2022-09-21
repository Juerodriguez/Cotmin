from django.shortcuts import render
from .form import ConsultForm
from ..Gestion.models import Tramites, TipoTramites


def index(request):
    return render(request, 'index.html')


def consultar(request):
    return render(request, 'consultar.html', {
        'form': ConsultForm()
    })


def consulta_realizada(request):
    tramite = Tramites.objects.get(tipo=request.POST["tipo"], number=request.POST["number"])
    return render(request, 'consulta_result.html', {
        'tramite': tramite
    })


def tramites(request):
    return render(request, 'tramites.html')
