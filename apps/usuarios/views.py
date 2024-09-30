from django.shortcuts import render, redirect
from django.contrib import messages
from firebase_admin import auth
from apps.tuPractica.models import Region, Comuna, Carrera
from .models import Usuario, Estudiante, Empresa
import firebase_admin
from django.http import JsonResponse


if not firebase_admin._apps:
    firebase_admin.initialize_app()


def registro_estudiante(request):
    regiones = Region.objects.all()  # Obtener todas las regiones
    comunas = Comuna.objects.all()   # Obtener todas las comunas
    carreras = Carrera.objects.all()  # Obtener todas las carreras

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        rut = request.POST.get('rut')
        region_id = request.POST.get('region')
        comuna_id = request.POST.get('comuna')
        carrera_id = request.POST.get('carrera')

        try:
            # usuario firebase
            user = auth.create_user(
                email=email,
                password=password
            )

            # usuario MySQL
            usuario = Usuario.objects.create(
                uid=user.uid,
                email=email,
                es_estudiante=True
            )

            # se obtienen los datos de las regiones, comunas y carreras
            region = Region.objects.get(id=region_id)
            comuna = Comuna.objects.get(id=comuna_id)
            carrera = Carrera.objects.get(id=carrera_id)

            # estudiante MySQL
            estudiante = Estudiante.objects.create(
                usuario=usuario,
                nombres=nombres,
                apellidos=apellidos,
                rut=rut,
                region=region,
                comuna=comuna,
                carrera=carrera
            )

            print(f"Estudiante creado: {estudiante}")
            messages.success(request, 'Estudiante registrado correctamente.')
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Error al registrar estudiante: {str(e)}')

    return render(request, 'usuario/registro_estudiante.html', {
        'regiones': regiones,
        'comunas': comunas,
        'carreras': carreras,
    })


def registro_empresa(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nombre_empresa = request.POST.get('nombre_empresa')
        rut = request.POST.get('rut')
        direccion = request.POST.get('direccion')

        try:
            # usuario firebase
            user = auth.create_user(
                email=email,
                password=password
            )

            # usuario MySQL
            usuario = Usuario.objects.create(
                uid=user.uid,
                email=email,
                es_estudiante=False
            )
            
            # empresa MySQL
            empresa = Empresa.objects.create(
                usuario=usuario,
                nombre_empresa=nombre_empresa,
                rut=rut,
                direccion=direccion
            )

            print(f"Empresa creada: {empresa}")
            messages.success(request, 'Empresa registrada correctamente.')
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Error al registrar empresa: {str(e)}')

    return render(request, 'usuario/registro_empresa.html')


def get_comunas(request, region_id):
    comunas = Comuna.objects.filter(region_id=region_id)
    comunas_list = list(comunas.values('id', 'nombre'))
    return JsonResponse(comunas_list, safe=False)


def seleccionar_tipo_usuario(request):
    if request.method == 'POST':
        tipo_usuario = request.POST.get('tipo_usuario')
        if tipo_usuario == 'estudiante':
            return redirect('registro_estudiante')
        elif tipo_usuario == 'empresa':
            return redirect('registro_empresa')
    return render(request, 'usuario/tipoUsuario.html')


def login(request):
    return render(request, 'usuario/login.html')
