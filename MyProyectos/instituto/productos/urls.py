from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('listar',views.listar, name='listar'),
    path('buscar',views.buscar, name='buscar'),
    path('buscar_id', views.buscar_id, name='buscar_id'),
    path('eliminar',views.eliminar, name='eliminar'),
    path('eliminar_id', views.eliminar_id, name='eliminar_id'),
    path('agregar',views.agregar, name='agregar'),
    path('editar',views.editar, name='editar'),
    path('formulario_editar',views.editar, name='formulario_editar'),
    path('menu',views.menu, name='menu'),
    path('menu_productos',views.menu_productos, name='menu_productos'),
    path('inicio',views.inicio, name='inicio'),
    path('inicio2',views.inicio2, name='inicio2'),
    path('productos',views.productos, name='productos'),
    path('calzado',views.calzado, name='calzado'),
    path('vestidos',views.vestidos, name='vestidos'),
    path('ropa',views.ropa, name='ropa'),
    path('accesorios',views.accesorios, name='accesorios'),
    path('registro',views.registro, name='registro'),
    path('iniciarSesion',views.iniciarSesion, name='iniciarSesion'),
    path('index',views.index, name='index'),
    path('admin',views.admin, name='admin'),
    path('mostrar_datos',views.mostrar_datos, name='mostrar_datos'),


]