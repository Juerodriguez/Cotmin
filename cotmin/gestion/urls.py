from django.urls import path
from . import views


urlpatterns = [
    path('registro/', views.register, name="register"),
    path('', views.home, name="home"),
    path('panel/', views.dashboard, name="panel"),
    path('salir/', views.signout, name="signout"),
    path('ingresar/', views.signin, name="signin"),
    path('tramites/', views.manage_tramite.as_view(), name="manage_tramite"),
    path('tramites/nuevo/', views.create_tramite, name="create_tramite"),
    path('tramites/search/', views.search_tramite, name="search_tramite"),
    path('tramites/order/<str:order>/', views.select_order, name="select_order"),
    path('tramites/<int:tramite_id>/', views.detail_tramite, name="detail_tramite"),
    path('tramites/<int:tramite_id>/modificar/', views.update_tramite, name="update_tramite"),
    path('tramites/<int:tramite_id>/borrar/', views.delete_tramite, name="delete_tramite"),
    path('tramites/<int:tramite_id>/completed/', views.completed_tramite, name="completed_tramite"),

]
