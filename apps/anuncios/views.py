# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AnuncioPractica
from .forms import AnuncioPracticaForm
from apps.tuPractica.models import Region, Comuna
from django.utils import timezone

# Crear un anuncio


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
                # Agregar esto para ver el error en la consola
                print(f"Error al crear el anuncio: {str(e)}")
        else:
            messages.error(
                request, "Por favor, verifica que todos los campos sean correctos.")
            # Agregar esto para ver los errores del formulario en la consola
            print("Formulario inválido:", form.errors)
    else:
        form = AnuncioPracticaForm()
    return render(request, 'anuncios/crear_anuncio.html', {
        'form': form,
        'regiones': regiones,
        'comunas': comunas
    })
# Editar un anuncio


@login_required
def modificar_anuncio(request, anuncio_id):
    anuncio = get_object_or_404(
        AnuncioPractica, id=anuncio_id, empresa=request.user.empresa)

    if request.method == 'POST':
        form = AnuncioPracticaForm(request.POST, instance=anuncio)
        if form.is_valid():
            form.save()
            messages.success(request, "Anuncio actualizado exitosamente.")
            return redirect('mis_anuncios')
    else:
        form = AnuncioPracticaForm(instance=anuncio)

    return render(request, 'anuncios/modificar_anuncio.html', {'form': form})

# Eliminar un anuncio


@login_required
def eliminar_anuncio(request, anuncio_id):
    anuncio = get_object_or_404(
        AnuncioPractica, id=anuncio_id, empresa=request.user.empresa)

    if request.method == 'POST':
        anuncio.delete()
        messages.success(request, "Anuncio eliminado exitosamente.")
        return redirect('mis_anuncios')

    return render(request, 'anuncios/eliminar_anuncio.html', {'anuncio': anuncio})

# Listar anuncios de la empresa


@login_required
def listar_anuncios(request):
    # Verificamos que el usuario autenticado sea una empresa
    if request.user.es_estudiante:
        messages.error(
            request, "No tienes permisos para acceder a esta página.")
        return redirect('home')

    # Obtenemos la empresa asociada al usuario autenticado
    empresa = request.user.empresa

    # Obtenemos todos los anuncios creados por la empresa
    anuncios = AnuncioPractica.objects.filter(empresa=empresa)

    return render(request, 'anuncios/listar_anuncios.html', {'anuncios': anuncios})
