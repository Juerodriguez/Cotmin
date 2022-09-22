from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
    path('tramites/', views.tramites, name='tramites'),
    path('consultar/', views.consultar, name='consultar'),
    path('consulta_result/', views.consulta_realizada, name='consulta_realizada')
]
