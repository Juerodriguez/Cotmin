from django.shortcuts import render, redirect
from .form import ConsultForm
#from ..Gestion.models import Tramites, TipoTramites


def index(request):
    return render(request, 'index.html')


def consultar(request):
    """
    Controlador para la vista de la consulta de tramite por el cliente

    :param request:
    :return:
    """
    return render(request, 'consultar.html', {
        'form': ConsultForm()
    })


def consulta_realizada(request):
    """
    Controlador para la vista que muestra la consulta si es encontrada

    :param request:
    :return:
    """
    try:
        tramite = Tramites.objects.get(tipo=request.POST["tipo"], number=request.POST["number"])
        return render(request, 'consulta_result.html', {
            'tramite': tramite
        })
    except:
        return redirect(request, 'consultar.html', {
            'error': 'Tramite no encontrado'
        })


def tramites(request):
    """
    Controlador que muestra la guia de tramites

    :param request:
    :return:
    """
    return render(request, 'tramites.html')
