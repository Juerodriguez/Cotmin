from django.urls import path
from . import views


urlpatterns = [
    path('registro/', views.register, name="register"),
    path('', views.home, name="home"),
    path('dashboard/', views.panel, name="dashboard"),
    path('salir/', views.signout, name="signout"),
    path('ingresar/', views.signin, name="signin")

]
