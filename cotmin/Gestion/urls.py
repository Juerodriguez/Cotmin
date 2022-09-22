from django.urls import path
from . import views


urlpatterns = [
    path('registro/', views.register, name="register"),
    path('', views.home, name="home"),
    path('dashboard/', views.panel, name="dashboard"),

]
