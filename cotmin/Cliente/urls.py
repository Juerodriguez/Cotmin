from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
    path('tramites/', views.tramites),
    path('consultar/', views.consultar),
    path('consulta_result/', views.consulta_realizada)
]