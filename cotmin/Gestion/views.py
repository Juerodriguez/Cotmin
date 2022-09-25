from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.utils import timezone
from django.http import HttpResponse
from .form import TramiteForm
from .models import Tramites


def home(request):
    """

    :param request:
    :return:

    Vista de inicio al entrar a la app, aqui encontramos el login
    """
    if request.user:
        return redirect('manage_tramite')
    return redirect('signin')


def dashboard(request):
    """

    :param request:
    :return:

    Controlador que muestra el panel principal una vez logeado el usuario
    """
    return render(request, 'panel.html')


@login_required
def detail_tramite(request, tramite_id):
    tramite = get_object_or_404(Tramites, pk=tramite_id)
    return render(request, 'detail.html', {
        'tramite': tramite,
    })


@login_required
def completed_tramite(request, tramite_id):
    tramite = get_object_or_404(Tramites, pk=tramite_id)
    if request.method == "POST":
        tramite.estado = "R"
        tramite.date_completed = timezone.now()
        tramite.completed_by = request.user.username
        tramite.save()
        return redirect('manage_tramite')


@login_required
def manage_tramite(request):
    tramites = Tramites.objects.all()
    return render(request, 'manage_tramites.html', {
        'tramites': tramites
    })


@login_required
def create_tramite(request):
    if request.method == "GET":
        return render(request, 'create_tramites.html', {
            'form': TramiteForm
        })
    elif request.method == "POST":
        try:
            form = TramiteForm(request.POST)
            new_tramite = form.save(commit=False)
            new_tramite.user = request.user
            new_tramite.save()
            return redirect("create_tramite")
        except ValueError:
            return render(request, 'create_tramites.html', {
                'form': TramiteForm,
                'error': "Ingresar valores correctos"
            })




@login_required
def update_tramite(request, tramite_id):
    if request.method == "GET":
        tramite = get_object_or_404(Tramites, pk=tramite_id)
        tramite.estado = "C"
        tramite.save()
        form = TramiteForm(instance=tramite)
        return render(request, 'update_tramite.html', {
            'form': form,
            'tramite': tramite,
        })
    elif request.method == "POST":
        if isinstance(request.user, User):
            try:
                tramite = get_object_or_404(Tramites, pk=tramite_id)
                form = TramiteForm(request.POST, instance=tramite)
                form.save()
                return redirect("detail_tramite", tramite_id)
            except ValueError:
                return render(request, 'update_tramites.html', {
                    'form': form,
                    'error': "Ingresar valores correctos"
                })


@login_required
def delete_tramite(request, tramite_id):
    tramite = get_object_or_404(Tramites, pk=tramite_id)
    if request.method == "POST" and isinstance(request.user, User):
        tramite.delete()
        return redirect('manage_tramite')


def register(request):
    """

    :param request:
    :return:

    Controlador para Vista de registro
    """
    if request.method == 'GET':
        # Enviar formulario a la vista
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    elif request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            # Registro de usuario
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('manage_tramite')
            except IntegrityError:
                return render(request, 'registro.html', {
                            'form': UserCreationForm,
                            'error': "Usuario ya existente"
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': "Las contraseñas no coinciden"
        })


@login_required
def signout(request):
    """
    Controlador para salir de la aplicacion

    :param request:
    :return:
    """
    logout(request)
    return redirect('home')


def signin(request):
    """
    Controlador para ingresar a la aplicacion

    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'signin.html', {
            'form': AuthenticationForm,
        })
    else:
        user = authenticate(request,
                            username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.hmtl', {
                'form': AuthenticationForm,
                'error': "Usuario o contraseña incorrecta"
            })
        else:
            login(request, user)
            return redirect('manage_tramite')
