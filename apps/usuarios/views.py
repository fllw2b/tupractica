from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Estudiante, Empresa, Region, Comuna, Carrera, Tag, Sector
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.db import transaction
from ..anuncios.models import AnuncioPractica
from .forms import EstudianteForm, EmpresaForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def registro_estudiante(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    carreras = Carrera.objects.all()
    habilidades = Tag.objects.all() 

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
        cv = request.FILES.get('cv')
        foto = request.FILES.get('foto')  
        habilidades_seleccionadas = request.POST.getlist('habilidades') 

        try:
            with transaction.atomic():

                usuario = Usuario.objects.create_user(
                    email=email,
                    password=password,
                    es_estudiante=True,
                    fecha_registro=timezone.now()
                )


                region = Region.objects.get(id=region_id)
                comuna = Comuna.objects.get(id=comuna_id)
                carrera = Carrera.objects.get(id=carrera_id)

                estudiante = Estudiante.objects.create(
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
                    telefono=telefono,
                    cv=cv,
                    foto=foto
                )

                for habilidad_id in habilidades_seleccionadas:
                    habilidad = Tag.objects.get(id=habilidad_id)
                    estudiante.habilidades.add(habilidad)

            messages.success(request, 'Te haz registrado correctamente.')
            return redirect('login')

        except Exception as e:
            messages.error(request, f'Error al registrar, inténtelo más tarde: {str(e)}')

    return render(request, 'usuario/registro_estudiante.html', {
        'regiones': regiones,
        'comunas': comunas,
        'carreras': carreras,
        'habilidades': habilidades,
    })



def registro_empresa(request):
    sectores = Sector.objects.all()

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nombre_empresa = request.POST.get('nombre_empresa')
        rut = request.POST.get('rut_empresa')
        direccion = request.POST.get('direccion')
        sector_id = request.POST.get('sector')
        pagina_web = request.POST.get('pagina_web', '')
        descripcion = request.POST.get('descripcion', '')
        redes_sociales = request.POST.get('redes_sociales', '')
        logo = request.FILES.get('logo')  

        try:
            with transaction.atomic():
                usuario = Usuario.objects.create_user(
                    email=email,
                    password=password,
                    es_estudiante=False,
                    fecha_registro=timezone.now()
                )

                sector = Sector.objects.get(id=sector_id)

                Empresa.objects.create(
                    usuario=usuario,
                    nombre_empresa=nombre_empresa,
                    rut=rut,
                    direccion=direccion,
                    sector=sector,
                    pagina_web=pagina_web,
                    descripcion=descripcion,
                    redes_sociales=redes_sociales,
                    logo=logo
                )

            messages.success(request, 'Empresa registrada correctamente.')
            return redirect('login')

        except Sector.DoesNotExist:
            messages.error(request, 'Error: El sector especificado no existe.')
        except Exception as e:
            messages.error(request, f'Error al registrar empresa: {str(e)}')

    return render(request, 'usuario/registro_empresa.html', {
        'sectores': sectores,
    })


def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        usuario = authenticate(request, username=email, password=password)

        if usuario is not None:
            auth_login(request, usuario)
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

@login_required
def perfil_estudiante(request, estudiante_id=None):
    if estudiante_id is None:
        estudiante = get_object_or_404(Estudiante, usuario=request.user)
        is_owner = True
    else:
        estudiante = get_object_or_404(Estudiante, id=estudiante_id)
        is_owner = (request.user == estudiante.usuario)

    if is_owner and request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect('perfil_estudiante')
    else:
        form = EstudianteForm(instance=estudiante)

    context = {
        'estudiante': estudiante,
        'form': form,
        'is_owner': is_owner,
    }
    return render(request, 'usuario/perfil_publico_estudiante.html', context)

@login_required
def perfil_empresa(request):
    # verificamos q sea una empresa y no estudiante
    if not hasattr(request.user, 'empresa'):
        messages.error(request, 'No tienes un perfil de empresa.')
        return redirect('home')

    empresa = request.user.empresa

    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfil_empresa')
        else:
            messages.error(request, 'Por favor, corrige los errores del formulario.')
    else:
        form = EmpresaForm(instance=empresa)

    # obtenemos los anuncios
    anuncios = AnuncioPractica.objects.filter(empresa=empresa).order_by('-fecha_publicacion')

    return render(request, 'empresas/perfil_empresa.html', {
        'empresa': empresa,
        'form': form,
        'anuncios': anuncios,
    })

def perfil_publico_empresa(request, empresa_id):
    # obtiene la empresa o lanza un 404 si no existe
    empresa = get_object_or_404(Empresa, id=empresa_id)

    # filtra los anuncios de la empresa
    anuncios = AnuncioPractica.objects.filter(empresa=empresa).order_by('-fecha_publicacion')

    return render(request, 'usuario/perfil_publico_empresa.html', {
        'empresa': empresa,
        'anuncios': anuncios
    })


@login_required
def editar_perfil_empresa(request):
    if not hasattr(request.user, 'empresa'):
        messages.error(request, 'No tienes un perfil de empresa.')
        return redirect('home')

    empresa = request.user.empresa

    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfil_empresa')
        else:
            messages.error(request, 'Por favor, corrige los errores del formulario.')
    else:
        form = EmpresaForm(instance=empresa)

    return render(request, 'empresas/editar_perfil_empresa.html', {
        'empresa': empresa,
        'form': form,
    })
