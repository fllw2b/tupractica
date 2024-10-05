from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Estudiante, Empresa, Region, Comuna, Carrera, Sector
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


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
        region_id = request.POST.get('region')
        comuna_id = request.POST.get('comuna')
        carrera_id = request.POST.get('carrera')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        genero = request.POST.get('genero')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')

        try:
            # creamos el user en la mysql
            usuario = Usuario.objects.create_user(
                email=email,
                password=password,
                es_estudiante=True,
                fecha_registro=timezone.now()
            )
            region = Region.objects.get(id=region_id)
            comuna = Comuna.objects.get(id=comuna_id)
            carrera = Carrera.objects.get(id=carrera_id)

            # creamos el estudiante en la mysql
            Estudiante.objects.create(
                usuario=usuario,
                nombres=nombres,
                apellidos=apellidos,
                rut=rut,
                region=region,
                comuna=comuna,
                carrera=carrera,
                fecha_nacimiento=fecha_nacimiento,
                genero=genero,
                direccion=direccion,
                telefono=telefono
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
        rut = request.POST.get('rut')
        direccion = request.POST.get('direccion')
        sector_id = request.POST.get('sector')
        pagina_web = request.POST.get('pagina_web')
        descripcion = request.POST.get('descripcion')
        redes_sociales = request.POST.get('redes_sociales')

        try:
            # creamos el user en la mysql
            usuario = Usuario.objects.create_user(
                email=email,
                password=password,
                es_estudiante=False,
                fecha_registro=timezone.now()
            )

            sector = Sector.objects.get(id=sector_id)

            # creamos la empresa en la mysql
            Empresa.objects.create(
                usuario=usuario,
                nombre_empresa=nombre_empresa,
                rut=rut,
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


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        usuario = authenticate(request, username=email, password=password)

        if usuario is not None:
            login(request, usuario)
            if usuario.es_estudiante:
                return redirect('home')
            else:
                return redirect('home')
        else:
            messages.error(
                request, 'Correo electrónico o contraseña incorrectos.')

    return render(request, 'usuario/login.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('home')


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
