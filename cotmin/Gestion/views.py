from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
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
