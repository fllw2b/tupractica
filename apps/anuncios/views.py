# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AnuncioPractica, Postulacion
from .forms import AnuncioPracticaForm
from apps.tuPractica.models import Region, Comuna
from apps.usuarios.models import Tag, Estudiante, Empresa, Usuario
from django.utils import timezone
from django.http import JsonResponse

@login_required
def crear_anuncio(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    tags = Tag.objects.all()

    if request.user.es_estudiante:
        messages.error(
            request, "No tienes permisos para acceder a esta página.")
        return redirect('home')

    if request.method == 'POST':
        form = AnuncioPracticaForm(request.POST)
        if form.is_valid():
            try:
                anuncio = form.save(commit=False)
                anuncio.empresa = request.user.empresa
                anuncio.fecha_publicacion = timezone.now()
                anuncio.region = Region.objects.get(
                    id=request.POST.get('region'))
                anuncio.comuna = Comuna.objects.get(
                    id=request.POST.get('comuna'))
                anuncio.save()
                form.save_m2m()
                messages.success(request, "Anuncio creado exitosamente.")
                return redirect('listar_anuncios')
            except Exception as e:
                messages.error(request, f"Error al crear el anuncio: {str(e)}")
                print(f"Error al crear el anuncio: {str(e)}")
        else:
            messages.error(
                request, "Por favor, verifica que todos los campos sean correctos.")
            print("Formulario inválido:", form.errors)
    else:
        form = AnuncioPracticaForm()
    
    return render(request, 'empresas/crear_anuncio.html', {
        'form': form,
        'regiones': regiones,
        'comunas': comunas,
        'tags': tags
    })


def modificar_anuncio(request, anuncio_id):
    anuncio = get_object_or_404(AnuncioPractica, id=anuncio_id, empresa=request.user.empresa)
    
    if request.method == 'POST':
        form = AnuncioPracticaForm(request.POST, instance=anuncio)
        if form.is_valid():
            anuncio = form.save(commit=False)  # aqui se guarda sin many2many o sin los tags
            anuncio.save()  
            form.save_m2m()  # aqui guardamos con many2many
            messages.success(request, "Anuncio modificado exitosamente.")
            return redirect('mis_anuncios')
        else:
            messages.error(request, "Hubo un error al modificar el anuncio. Por favor, revisa los datos ingresados.")
    else:
        form = AnuncioPracticaForm(instance=anuncio)
    
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    tags = Tag.objects.all()
    
    return render(request, 'empresas/modificar_anuncio.html', {
        'form': form,
        'regiones': regiones,
        'comunas': comunas,
        'tags': tags, 
    })

def detalle_anuncio(request, anuncio_id):
    # get_object_or_404 pa obtener el anuncio o mostrar un error 404 si no existe o no lo pilla
    anuncio = get_object_or_404(AnuncioPractica, id=anuncio_id)
    
    context = {
        'anuncio': anuncio
    }
    return render(request, 'anuncios/detalle_anuncio.html', context)

@login_required
def eliminar_anuncio(request, anuncio_id):
    anuncio = get_object_or_404(AnuncioPractica, id=anuncio_id, empresa=request.user.empresa)
    
    if request.method == 'POST':
        anuncio.delete()
        messages.success(request, "El anuncio ha sido eliminado exitosamente.")
        return redirect('mis_anuncios')
    else:
        return render(request, 'empresas/confirmar_eliminar.html', {'anuncio': anuncio})


@login_required
def mis_anuncios(request):
    if request.user.is_authenticated and hasattr(request.user, 'empresa'):
        empresa = request.user.empresa
        anuncios = AnuncioPractica.objects.filter(empresa=empresa)
        return render(request, 'empresas/mis_anuncios.html', {'anuncios': anuncios})
    else:
        return redirect('login')

def listar_anuncios(request):
    anuncios = AnuncioPractica.objects.all()
    busqueda = request.GET.get('busqueda', '')
    region = request.GET.get('region', '')
    modalidad = request.GET.get('modalidad', '')

    # Aplicar los filtros
    if busqueda:
        anuncios = anuncios.filter(titulo__icontains=busqueda)
    
    if region:
        anuncios = anuncios.filter(region__nombre=region)
    
    if modalidad:
        anuncios = anuncios.filter(modalidad__iexact=modalidad)

    recomendaciones = []

    # Verificar si el usuario es estudiante para calcular el porcentaje de coincidencia y si ya postuló
    if hasattr(request.user, 'estudiante'):
        estudiante = request.user.estudiante
        habilidades_estudiante = set(estudiante.habilidades.all())

        for anuncio in anuncios:
            # Calcular porcentaje de coincidencia
            requisitos_anuncio = set(anuncio.requisitos.all())
            habilidades_comunes = habilidades_estudiante.intersection(requisitos_anuncio)
            total_requisitos = len(requisitos_anuncio)
            if total_requisitos > 0:
                porcentaje_coincidencia = int((len(habilidades_comunes) / total_requisitos) * 100)
            else:
                porcentaje_coincidencia = 0

            # Verificar si ya postuló
            ya_postulo = Postulacion.objects.filter(estudiante=estudiante, anuncio=anuncio).exists()

            recomendaciones.append({
                'anuncio': anuncio,
                'porcentaje_coincidencia': porcentaje_coincidencia,
                'ya_postulo': ya_postulo
            })

        # Ordenar por porcentaje de coincidencia
        recomendaciones.sort(key=lambda x: x['porcentaje_coincidencia'], reverse=True)
    else:
        # Si no es estudiante, mostrar los anuncios sin el porcentaje
        for anuncio in anuncios:
            recomendaciones.append({
                'anuncio': anuncio,
                'porcentaje_coincidencia': None,  # ocultar el porcentaje
                'ya_postulo': False
            })

    return render(request, 'anuncios/listar_anuncios.html', {
        'recomendaciones': recomendaciones,
        'busqueda': busqueda,
        'region': region,
        'modalidad': modalidad
    })
@login_required
def postular_anuncio(request, anuncio_id):
    # para que solo estudiantes puedan postular IMPORTANTE!!
    if not hasattr(request.user, 'estudiante'):
        messages.error(request, "Solo los estudiantes pueden postular a un anuncio.")
        return redirect('listar_anuncios')

    anuncio = get_object_or_404(AnuncioPractica, id=anuncio_id)
    estudiante = request.user.estudiante

    # para q no se dupliquen las postulaciones
    if Postulacion.objects.filter(estudiante=estudiante, anuncio=anuncio).exists():
        messages.info(request, "Ya has postulado a este anuncio.")
    else:
        Postulacion.objects.create(estudiante=estudiante, anuncio=anuncio)
        messages.success(request, "Postulación realizada exitosamente.")

    return redirect('listar_anuncios')

@login_required
def historial_postulaciones(request):
    if not hasattr(request.user, 'estudiante'):
        messages.error(request, "Solo los estudiantes pueden ver su historial de postulaciones.")
        return redirect('lista_anuncios')

    postulaciones = Postulacion.objects.filter(estudiante=request.user.estudiante).select_related('anuncio')
    
    return render(request, 'estudiantes/historial_postulaciones.html', {'postulaciones': postulaciones})

@login_required
def postulaciones_empresa(request):
    if not hasattr(request.user, 'empresa'):
        messages.error(request, "Solo las empresas pueden acceder a esta sección.")
        return redirect('lista_anuncios')

    anuncios = AnuncioPractica.objects.filter(empresa=request.user.empresa).prefetch_related('postulantes__estudiante__usuario')
    
    return render(request, 'empresas/postulaciones_empresa.html', {'anuncios': anuncios})

@login_required
def recomendaciones_estudiante(request):
    # verificamos q el user sea estudiante
    if not hasattr(request.user, 'estudiante'):
        messages.error(request, "No tienes permisos para acceder a esta página.")
        return redirect('home')

    estudiante = request.user.estudiante
    anuncios = AnuncioPractica.objects.all()
    recomendaciones = []

    # obtenemos las habilidades o tags
    habilidades_estudiante = set(estudiante.habilidades.all())

    for anuncio in anuncios:
        # obtenemos los requisitos o tags del anuncio
        requisitos_anuncio = set(anuncio.requisitos.all())
        # calculamos la coincidencia
        habilidades_comunes = habilidades_estudiante.intersection(requisitos_anuncio)
        total_requisitos = len(requisitos_anuncio)
        if total_requisitos > 0:
            porcentaje_coincidencia = int((len(habilidades_comunes) / total_requisitos) * 100)
        else:
            porcentaje_coincidencia = 0
        
        # lo agregamos a la lista de recomendaciones
        recomendaciones.append({
            'anuncio': anuncio,
            'porcentaje_coincidencia': porcentaje_coincidencia
        })

    # ordenamos por % desc
    recomendaciones.sort(key=lambda x: x['porcentaje_coincidencia'], reverse=True)

    return render(request, 'anuncios/recomendaciones_estudiante.html', {
        'recomendaciones': recomendaciones
    })


def detalle_anuncio_ajax(request, anuncio_id):
    anuncio = get_object_or_404(AnuncioPractica, id=anuncio_id)
    return render(request, 'anuncios/detalle_anuncio_ajax.html', {'anuncio': anuncio})

@login_required
def eliminar_postulacion(request, postulacion_id):
    if request.method == 'POST':
        try:
            print(f"Intentando eliminar la postulación con ID: {postulacion_id}")
            postulacion = get_object_or_404(Postulacion, id=postulacion_id, estudiante=request.user.estudiante)
            postulacion.delete()
            messages.success(request, "Postulación eliminada exitosamente.")
        except Exception as e:
            messages.error(request, "Ocurrió un error al intentar eliminar la postulación.")
            print(e)  # imprimimos el error
    return redirect('historial_postulaciones')