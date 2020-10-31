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

def listar(request):
    print("Estamos en la vista listar")
    context={}
    return render(request,'productos/listar.html',context)

def mostrar_alumnos(request):
    print("Estamos en la vista mostrar alumnos")
    #lista = Alumno.objects.all()
    lista = Alumno.objects.filter(activo = 1, genero = 'femenino')
    context={'listado':lista}
    return render(request,'productos/listar_alumnos.html',context)

def buscar(request):
    print("Estamos en la vista buscar")
    context={}
    return render(request,'productos/boton_buscar.html',context)

def buscar_por_rut(request):
    print("Estamos en la vista buscar por rut")
    try:
        mi_rut=request.POST['rut']
        alumno = Alumno.objects.get(rut = mi_rut)
    except Alumno.DoesNotExist:
        messages.error(request, "Alumno No existe")
        context = {}
        return render(request, 'productos/boton_buscar.html', context)

    context = {'alumno': alumno}
    return render(request, 'productos/mostrar_datos.html', context)

def eliminar(request):
    print("Estamos en la vista eliminar")
    context={}
    return render(request,'productos/boton_eliminar.html',context)


def eliminar_por_rut(request):

    print("hola  estoy en eliminar_por_rut...")
    if request.method == 'POST':
        mi_rut = request.POST['rut']

        if mi_rut != "":
            try:
                alumno = Alumno()
                alumno = Alumno.objects.get(rut=mi_rut)
                if alumno is not None:
                    print("Alumno=", alumno)
                    alumno.delete()
                    context = {}
                    return render(request, 'productos/mensaje_alumno_eliminado.html', context)
                else:
                    return render(request, 'productos/error/error2.html', {})
            except alumno.DoesNotExist:
                return render(request, 'productos/error/error2.html', {})
        else:
            return render(request, 'productos/error/error1.html', {})
    else:
        return render(request, 'productos/error/error3.html', {})

def agregar(request):
    print("Estamos en la vista agregar")
    context = {}
    return render(request, 'productos/formulario_agregar.html', context)

def agregar_alumno(request):
    print("hola  estoy en agregar_alumno...")
    if request.method == 'POST':
       mi_rut = request.POST['rut']
       mi_nombre= request.POST['nombre']
       mi_paterno=request.POST['aPaterno']
       mi_materno=request.POST['aMaterno']
       mi_fechaNac =request.POST['fechaNac']
       mi_genero=request.POST['genero']
       mi_foto = request.FILES['foto']

       if mi_rut != "":
           try:
               alumno = Alumno()

               alumno.rut = mi_rut
               alumno.nombre = mi_nombre
               alumno.apellido_paterno = mi_paterno
               alumno.apellido_materno = mi_materno
               alumno.fecha_nacimiento = mi_fechaNac
               alumno.genero = mi_genero
               alumno.foto = mi_foto

               alumno.save()

               return render(request, 'productos/mensaje_datos_grabados.html',{})

           except alumno.DoesNotExist:
               return render(request, 'productos/error/error4.html', {})
       else:
           return render(request, 'productos/error/error1.html', {})
    else:
        return render(request, 'productos/error/error3.html', {})

def editar(request):
    print("Estamos en la vista editar")
    context = {}
    return render(request, 'productos/boton_editar.html', context)

def buscar_para_editar(request):
    print("Estamos en la vista buscar para editar")
    if request.method == 'POST':
        mi_rut = request.POST['rut']

        if mi_rut != "":
            try:
                alumno = Alumno()
                alumno = Alumno.objects.get(rut=mi_rut)
                if alumno is not None:
                    print("Alumno=", alumno)
                    context = {'alumno': alumno}

                    return render(request, 'productos/formulario_editar.html', context)
                else:
                    return render(request, 'productos/error/error2.html', {})
            except alumno.DoesNotExist:
                return render(request, 'productos/error/error2.html', {})
        else:
            return render(request, 'productos/error/error1.html', {})
    else:
        return render(request, 'productos/error/error3.html', {})

def actualizar_alumno(request):
    print("hola  estoy en actualizar_alumno...")
    if request.method == 'POST':
       mi_id = request.POST['id_alumno']
       mi_rut = request.POST['rut']
       mi_nombre= request.POST['nombre']
       mi_paterno=request.POST['aPaterno']
       mi_materno=request.POST['aMaterno']
       mi_fechaNac =request.POST['fechaNac']
       mi_genero=request.POST['genero']
       mi_foto = request.FILES['foto']

       if mi_rut != "":
           try:
               alumno = Alumno()

               alumno.id_alumno = mi_id
               alumno.rut = mi_rut
               alumno.nombre = mi_nombre
               alumno.apellido_paterno = mi_paterno
               alumno.apellido_materno = mi_materno
               alumno.fecha_nacimiento = mi_fechaNac
               alumno.genero = mi_genero
               alumno.activo = 1
               alumno.foto = mi_foto

               alumno.save() #actualiza

               return render(request, 'productos/mensaje_datos_grabados.html',{})

           except alumno.DoesNotExist:
               return render(request, 'productos/error/error4.html', {})
       else:
           return render(request, 'productos/error/error1.html', {})
    else:
        return render(request, 'productos/error/error3.html', {})

def menu(request):
    print("Estamos en la vista menu ")
    alumnos = Alumno.objects.all()
    context={'alumnos':alumnos}
    return render(request,'productos/menu_alumno.html',context)

def menu_productos(request):
    print("Estamos en la vista menu productos ")
    alumnos = Alumno.objects.all()
    context={'alumnos':alumnos}
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
