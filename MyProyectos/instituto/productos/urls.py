from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('accesorios',views.accesorios, name='accesorios'),
    path('admin',views.admin, name='admin'),
    path('boton_buscar',views.boton_buscar, name='boton_buscar'),
    path('boton_editar',views.boton_editar, name='boton_editar'),
    path('boton_eliminar', views.boton_eliminar, name='boton_eliminar'),
    path('buscar', views.buscar, name='buscar'),
    path('buscar_id', views.buscar_id, name='buscar_id'),
    path('listar',views.listar, name='listar'),
    path('eliminar', views.eliminar, name='eliminar'),
    path('eliminar_id',views.eliminar_id, name='eliminar_id'),
    path('agregar',views.agregar, name='agregar'),
    path('agregar_datos', views.agregar_datos, name='agregar_datos'),
    path('editar',views.editar, name='editar'),
    path('buscar_editar', views.buscar_editar, name='buscar_editar'),
    path('actualizar_datos',views.actualizar_datos, name='actualizar_datos'),
    path('menu', views.menu, name='menu'),
    path('calzado',views.calzado, name='calzado'),
    path('formulario_agregar',views.agregar, name='formulario_agregar'),
    path('formulario_editar',views.editar, name='formulario_editar'),
    path('iniciarSesion',views.iniciarSesion, name='iniciarSesion'),
    path('inicio',views.inicio, name='inicio'),
    path('inicio2',views.inicio2, name='inicio2'),
    path('leciel', views.leciel, name='leciel'),
    path('listar',views.listar, name='listar'),
    path('listar_datos',views.listar_datos, name='listar_datos'),
    path('mensaje_datos_grabados',views.mensaje_datos_grabados, name='mensaje_datos_grabados'),
    path('mensaje_eliminado', views.mensaje_eliminado, name='mensaje_eliminado'),
    path('menu_productos',views.menu_productos, name='menu_productos'),
    path('mostrar_datos',views.mostrar_datos, name='mostrar_datos'),
    path('productos',views.productos, name='productos'),
    path('registro',views.registro, name='registro'),
    path('ropa',views.ropa, name='ropa'),
    path('vestidos',views.vestidos, name='vestidos'),




]