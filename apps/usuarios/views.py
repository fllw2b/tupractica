from django.shortcuts import render, redirect
from django.contrib import messages
from firebase_admin import auth
from apps.tuPractica.models import Region, Comuna, Carrera, Sector
from .models import Usuario, Estudiante, Empresa
import firebase_admin
from django.http import JsonResponse
import re


if not firebase_admin._apps:
    firebase_admin.initialize_app()


def registro_estudiante(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    carreras = Carrera.objects.all()

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        rut = request.POST.get('rut')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        genero = request.POST.get('genero')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        region_id = request.POST.get('region')
        comuna_id = request.POST.get('comuna')
        carrera_id = request.POST.get('carrera')
        foto = request.FILES.get('foto')

        try:
            # usuario firebase
            user = auth.create_user(
                email=email,
                password=password
            )

            # usuario mysql
            usuario = Usuario.objects.create(
                uid=user.uid,
                email=email,
                es_estudiante=True
            )

            # región, comuna y carrera
            region = Region.objects.get(id=region_id)
            comuna = Comuna.objects.get(id=comuna_id)
            carrera = Carrera.objects.get(id=carrera_id)

            # se crea en la mysql
            estudiante = Estudiante.objects.create(
                usuario=usuario,
                nombres=nombres,
                apellidos=apellidos,
                rut=rut,
                fecha_nacimiento=fecha_nacimiento,
                genero=genero,
                direccion=direccion,
                telefono=telefono,
                region=region,
                comuna=comuna,
                carrera=carrera,
                foto=foto
            )

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
    sectores = Sector.objects.all()

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nombre_empresa = request.POST.get('nombre_empresa')
        rut_empresa = request.POST.get('rut_empresa')
        direccion = request.POST.get('direccion')
        sector_id = request.POST.get('sector')
        pagina_web = request.POST.get('pagina_web')
        descripcion = request.POST.get('descripcion')
        redes_sociales = request.POST.get('redes_sociales')

        try:
            # usuario firebase
            user = auth.create_user(
                email=email,
                password=password
            )

            # usuario mysql
            usuario = Usuario.objects.create(
                uid=user.uid,
                email=email,
                es_estudiante=False
            )

            # se obtienen los sectores
            sector = Sector.objects.get(id=sector_id)

            # se  crea en la mysql
            empresa = Empresa.objects.create(
                usuario=usuario,
                nombre_empresa=nombre_empresa,
                rut=rut_empresa,
                direccion=direccion,
                sector=sector,
                pagina_web=pagina_web,
                descripcion=descripcion,
                redes_sociales=redes_sociales
            )

            messages.success(request, 'Empresa registrada correctamente.')
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Error al registrar empresa: {str(e)}')

    return render(request, 'usuario/registro_empresa.html', {
        'sectores': sectores,
    })


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
