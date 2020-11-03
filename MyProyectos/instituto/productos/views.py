from django.contrib import messages
from django.shortcuts import render
from .models import Alumno


# Create your views here.


def index(request):
    print("Estamos en la vista")
    context={}
    return render(request,'productos/index.html',context)

def inicio(request):
    print("Estamos en inicio")
    context={}
    return render(request,'productos/inicio.html',context)

def inicio2(request):
    print("Estamos en inicio")
    context={}
    return render(request,'productos/inicio2.html',context)

def listar(request):
    print("Estamos en la vista listar")
    context={}
    return render(request,'productos/listar.html',context)

def mostrar_datos(request):
    print("ok, estamos en mostrar_datos")
    listar = Alumno.objects.all()
    context={'listado':listar}
    return render(request, 'productos/listar_datos.html', context)

def buscar(request):
    print("Estamos en la vista buscar")
    context={}
    return render(request,'productos/boton_buscar.html',context)

def productos(request):
    print("Estamos en la vista productos")
    context={}
    return render(request,'productos/productos.html',context)

def buscar_id (request):
    print("hola  estoy en buscar_id...")
    if request.method == 'POST':
       mi_id = request.POST['id']

       if mi_id != "":
           try:
               datos = datos()
               datos= Datos.objects.get(id=mi_id)
               if datos is not None:
                   print("Datos=", datos)
                   context={'datos':datos}
                   return render(request, 'productos/mostrar_datos.html', context)
               else:
                   return render(request, 'productos/error/error_202.html',{})
           except datos.DoesNotExist:
               return render(request, 'productos/error/error_202.html', {})
       else:
           return render(request, 'productos/error/error_201.html', {})
    else:
        return render(request, 'productos/error/error_203.html', {})

def eliminar(request):
    print("Estamos en la vista eliminar")
    context={}
    return render(request,'productos/boton_eliminar.html',context)


def eliminar_id(request):

    print("hola  estoy en eliminar_id...")
    if request.method == 'POST':
        mi_id = request.POST['id']

        if mi_id != "":
            try:
                datos = Datos()
                datos = Datos.objects.get(id = mi_id)
                if datos is not None:
                    print("Datos=", datos)
                    datos.delete()
                    context={}
                    return render(request, 'productos/mensaje_eliminado.html',context)
                else:
                    return render(request, 'productos/error/error_202.html', {})
            except datos.DoesNotExist:
                return render(request, 'productos/error/error_202.html', {})
        else:
            return render(request, 'productos/error/error_201.html', {})
    else:
        return render(request, 'productos/error/error_203.html', {})

def agregar(request):
    print("Estamos en la vista agregar")
    context = {}
    return render(request, 'productos/formulario_agregar.html', context)

def agregar_datos(request):
    print("hola  estoy en agregar_datos...")
    if request.method == 'POST':
       mi_id = request.POST['id']
       mi_numero = request.POST['numero']
       mi_nombre = request.POST['nombre']
       mi_precio = request.POST['precio']
       mi_stock = request.POST['stock']
       mi_foto = request.FILES['foto']
       mi_tipo = request.POST['tipo']

       if mi_id != "":
           try:
               datos = Datos()

               producto = Producto()
               producto.numero = mi_numero
               producto.nombre = mi_nombre
               producto.precio = mi_precio
               producto.foto = mi_foto
               producto.stock = mi_stock
               producto.activo = 1
               producto.tipo = mi_tipo

               datos.save()

               return render(request, 'productos/mensaje_datos_grabados.html',{})

           except datos.DoesNotExist:
               return render(request, 'productos/error/error_204.html', {})
       else:
           return render(request, 'productos/error/error_201.html', {})
    else:
        return render(request, 'productos/error/error_203.html', {})

def editar(request):
    print("Estamos en la vista editar")
    context = {}
    return render(request, 'productos/boton_editar.html', context)

def formulario_editar(request):
    print("Estamos en la vista editar")
    context = {}
    return render(request, 'productos/boton_editar.html', context)

def buscar_editar(request):
    print("hola  estoy en buscar_editar...")
    if request.method == 'POST':
       mi_rut = request.POST['id']

       if mi_id != "":
           try:
               datos = Datos()
               datos= Datos.objects.get(id=mi_id)
               if datos is not None:
                   print("Datos=", datos)
                   context={'datos':datos}
                   return render(request, 'productos/formulario_editar.html', context)
               else:
                   return render(request, 'productos/error/error_202.html',{})
           except datos.DoesNotExist:
               return render(request, 'productos/error/error_202.html', {})
       else:
           return render(request, 'productos/error/error_201.html', {})
    else:
        return render(request, 'productos/error/error_203.html', {})

def actualizar_datos(request):
    print("hola  estoy en actualizar_datos...")
    if request.method == 'POST':
       mi_id = request.POST['id']
       mi_numero = request.POST['numero']
       mi_precio = request.POST['precio']
       mi_nombre = request.POST['nombre']
       mi_foto = request.FILES['foto']
       mi_stock = request.POST['stock']
       mi_tipo = request.POST['tipo']

       if mi_id != "":
           try:
               datos = Datos()
               datos.id_datos = mi_id
               producto.numero = mi_numero
               producto.precio = mi_precio
               producto.nombre = mi_nombre
               producto.foto = mi_foto
               producto.stock = mi_stock
               producto.tipo = mi_tipo
               datos.activo = 1

               datos.save()  #actualiza

               return render(request, 'productos/mensaje_datos_grabados.html',{})

           except datos.DoesNotExist:
               return render(request, 'productos/error/error_204.html', {})
       else:
           return render(request, 'productos/error/error_201.html', {})
    else:
        return render(request, 'productos/error/error_203.html', {})

def menu(request):
    print("Estamos en la vista menu ")
    alumnos = Datos.objects.all()
    context={'datos':datos}
    return render(request,'productos/menu_productos.html',context)

def menu_productos(request):
    print("Estamos en la vista menu productos ")
    alumnos = Datos.objects.all()
    context={'datos':datos}
    return render(request,'productos/menu_productos.html',context)

def productos(request):
    print("Estamos en productos")
    context={}
    return render(request,'productos/productos.html',context)

def calzado(request):
    print("Estamos en calzados")
    context={}
    return render(request,'productos/calzado.html',context)

def vestidos(request):
    print("Estamos en vestidos")
    context={}
    return render(request,'productos/vestidos.html',context)

def ropa(request):
    print("Estamos en ropa")
    context={}
    return render(request,'productos/ropa.html',context)

def accesorios(request):
    print("Estamos en accesorios")
    context={}
    return render(request,'productos/accesorios.html',context)

def registro(request):
    print("Estamos en registro")
    context={}
    return render(request,'productos/registro.html',context)

def iniciarSesion(request):
    print("Estamos en iniciarSesion")
    context={}
    return render(request,'productos/iniciarSesion.html',context)

def index(request):
    print("Estamos en index")
    context={}
    return render(request,'productos/index.html',context)

def admin(request):
    print("Estamos en la vista listar")
    context={}
    return render(request,'productos/admin.html',context)


def boton_buscar():
    print("Estamos en la vista boton buscar")
    context = {}
    return render(request, 'productos/boton_buscar.html', context)


def boton_editar():
    print("Estamos en la vista boton editar")
    context = {}
    return render(request, 'productos/boton_editar.html', context)

def boton_eliminar():
    print("Estamos en la vista boton eliminar")
    context = {}
    return render(request, 'productos/boton_eliminar.html', context)


def leciel():
    print("Estamos en la vista leciel")
    context = {}
    return render(request, 'productos/leciel.html', context)


def listar_datos():
    print("Estamos en la vista listar_datos")
    context = {}
    return render(request, 'productos/listar_datos.html', context)


def mensaje_datos_grabados():
    print("Estamos en la vista mensaje_datos_grabados")
    context = {}
    return render(request, 'productos/mensaje_datos_grabados.html', context)


def mensaje_eliminado():
    print("Estamos en la vista mensaje_eliminado")
    context = {}
    return render(request, 'productos/mensaje_eliminado.html', context)
