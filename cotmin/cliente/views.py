from django.shortcuts import render, redirect
from .form import ConsultForm
from gestion.models import Tramites, TipoTramites
from django.http import Http404


def index():
    return redirect('tramites')


def consultar(request):
    """
    Controlador para la vista de la consulta de tramite por el cliente

    :param request:
    :return:
    """
    # TODO: Mejorar mostrando opciones de tipo de tramites
    return render(request, 'consultar.html', {
        'form': ConsultForm()
    })


def consulta_realizada(request):
    """
    Controlador para la vista que muestra la consulta si es encontrada

    :param request:
    :return:
    """
    # TODO: Mostrar a profundidad todo el detalle, en especial el estado del tramite
    try:
        tramite = Tramites.objects.get(tipo=request.POST["tipo"], number=request.POST["number"])
        return render(request, 'consulta_result.html', {
            'tramite': tramite
        })
    except Tramites.DoesNotExist:
        raise Http404("Este tramite no existe")


def tramites(request):
    """
    Controlador que muestra la guia de tramites

    :param request:
    :return:
    """
    return render(request, 'tramites.html')
