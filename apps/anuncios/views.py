# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AnuncioPractica, Postulacion
from .forms import AnuncioPracticaForm
from apps.tuPractica.models import Region, Comuna
from django.utils import timezone
from django.core.paginator import Paginator


@login_required
def crear_anuncio(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()

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
        'comunas': comunas
    })


def modificar_anuncio(request, anuncio_id):
    anuncio = get_object_or_404(AnuncioPractica, id=anuncio_id, empresa=request.user.empresa)
    
    if request.method == 'POST':
        form = AnuncioPracticaForm(request.POST, instance=anuncio)
        if form.is_valid():
            form.save() 
            messages.success(request, "Anuncio modificado exitosamente.")
            return redirect('mis_anuncios') 
        else:
            messages.error(request, "Hubo un error al modificar el anuncio. Por favor, revisa los datos ingresados.")
    else:
        form = AnuncioPracticaForm(instance=anuncio)
    #cargamos regiones y comunas para que los dropbox no salgan vacios
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    
    return render(request, 'empresas/modificar_anuncio.html', {
        'form': form,
        'regiones': regiones,
        'comunas': comunas,
    })

def detalle_anuncio(request, anuncio_id):
    # Utilizamos get_object_or_404 para obtener el anuncio o mostrar un error 404 si no existe
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
    if request.user.es_estudiante:
        messages.error(
            request, "No tienes permisos para acceder a esta página.")
        return redirect('home')

    empresa = request.user.empresa

    anuncios = AnuncioPractica.objects.filter(empresa=empresa)

    return render(request, 'empresas/mis_anuncios.html', {'anuncios': anuncios})

# def lista_anuncios(request):
#     query = request.GET.get('q')
#     anuncios_list = AnuncioPractica.objects.all()

#     if query:
#         anuncios_list = anuncios_list.filter(titulo__icontains=query)

#     paginator = Paginator(anuncios_list, 10)
#     page_number = request.GET.get('page')
#     anuncios = paginator.get_page(page_number)

#     return render(request, 'anuncios/lista_anuncios.html', {'anuncios': anuncios})


# def detalle_anuncio(request, anuncio_id):
#     anuncio = get_object_or_404(AnuncioPractica, id=anuncio_id)
#     return render(request, 'anuncios/detalle_anuncio.html', {'anuncio': anuncio})

def listar_anuncios(request):
    busqueda = request.GET.get('busqueda', '')
    region = request.GET.get('region', '')
    modalidad = request.GET.get('modalidad', '')
    
    anuncios = AnuncioPractica.objects.all()
    
    if busqueda:
        anuncios = anuncios.filter(titulo__icontains=busqueda)
    
    if region:
        anuncios = anuncios.filter(region__nombre__iexact=region)
    
    if modalidad:
        anuncios = anuncios.filter(modalidad__iexact=modalidad)

    context = {
        'anuncios': anuncios,
        'busqueda': busqueda,
        'region': region,
        'modalidad': modalidad,
    }
    return render(request, 'anuncios/listar_anuncios.html', context)

@login_required
def postular_anuncio(request, anuncio_id):
    # para que solos los estudiantes puedan postular IMPORTANTE!!!
    if not hasattr(request.user, 'estudiante'):
        messages.error(request, "Solo los estudiantes pueden postular a un anuncio.")
        return redirect('lista_anuncios')

    anuncio = get_object_or_404(AnuncioPractica, id=anuncio_id)
    estudiante = request.user.estudiante

    # para que no se dupliquen las postulaciones
    if Postulacion.objects.filter(estudiante=estudiante, anuncio=anuncio).exists():
        messages.info(request, "Ya has postulado a este anuncio.")
    else:
        Postulacion.objects.create(estudiante=estudiante, anuncio=anuncio)
        messages.success(request, "Postulación realizada exitosamente.")

    return redirect('lista_anuncios')

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


