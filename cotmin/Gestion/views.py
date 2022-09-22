from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse


def home(request):
    """

    :param request:
    :return:

    Vista de inicio al entrar a la app, aqui encontramos el login
    """
    return render(request, 'index.html')


def panel(request):
    """

    :param request:
    :return:

    Vista que muestra el panel principal una vez logeado el usuario
    """
    return render(request, 'dashboard.html')


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
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'registro.html', {
                            'form': UserCreationForm,
                            'error': "Usuario ya existente"
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': "Las contraseñas no coinciden"
        })


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
            return redirect('dashboard')
