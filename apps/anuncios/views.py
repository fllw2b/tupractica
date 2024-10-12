# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AnuncioPractica
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
    return render(request, 'anuncios/crear_anuncio.html', {
        'form': form,
        'regiones': regiones,
        'comunas': comunas
    })


@login_required
def modificar_anuncio(request, anuncio_id):
    try:
        anuncio = AnuncioPractica.objects.get(id=anuncio_id, empresa=request.user.empresa)
    except AnuncioPractica.DoesNotExist:
        messages.error(request, "El anuncio no existe o no tienes permisos para modificarlo.")
        return redirect('mis_anuncios')

    if request.method == 'POST':
        form = AnuncioPracticaForm(request.POST, instance=anuncio)
        if form.is_valid():
            anuncio = form.save(commit=False)
            # Manejar los campos de región y comuna
            anuncio.region = Region.objects.get(id=request.POST.get('region'))
            anuncio.comuna = Comuna.objects.get(id=request.POST.get('comuna'))
            anuncio.save()
            messages.success(request, "Anuncio modificado exitosamente.")
            return redirect('mis_anuncios')
        else:
            print(form.errors)  # Esto imprimirá cualquier error de validación.
            messages.error(request, "Por favor, revisa los campos del formulario.")
    else:
        form = AnuncioPracticaForm(instance=anuncio)

    regiones = Region.objects.all()
    comunas = Comuna.objects.all()

    return render(request, 'anuncios/modificar_anuncio.html', {
        'form': form,
        'regiones': regiones,
        'comunas': comunas,
        'anuncio': anuncio,  # Asegúrate de pasar el anuncio a la plantilla
    })


@login_required
def eliminar_anuncio(request, anuncio_id):
    anuncio = get_object_or_404(AnuncioPractica, id=anuncio_id, empresa=request.user.empresa)
    
    if request.method == 'POST':
        anuncio.delete()
        messages.success(request, "El anuncio ha sido eliminado exitosamente.")
        return redirect('listar_anuncios')  # Redirige a la lista de anuncios del usuario
    else:
        return render(request, 'anuncios/confirmar_eliminar.html', {'anuncio': anuncio})



@login_required
def mis_anuncios(request):
    if request.user.es_estudiante:
        messages.error(
            request, "No tienes permisos para acceder a esta página.")
        return redirect('home')

    empresa = request.user.empresa

    anuncios = AnuncioPractica.objects.filter(empresa=empresa)

    return render(request, 'anuncios/mis_anuncios.html', {'anuncios': anuncios})

def lista_anuncios(request):
    query = request.GET.get('q')
    anuncios_list = AnuncioPractica.objects.all()

    if query:
        anuncios_list = anuncios_list.filter(titulo__icontains=query)

    # Agrega filtros adicionales si es necesario

    paginator = Paginator(anuncios_list, 10)
    page_number = request.GET.get('page')
    anuncios = paginator.get_page(page_number)

    return render(request, 'anuncios/lista_anuncios.html', {'anuncios': anuncios})


def detalle_anuncio(request, anuncio_id):
    anuncio = get_object_or_404(AnuncioPractica, id=anuncio_id)
    return render(request, 'anuncios/detalle_anuncio.html', {'anuncio': anuncio})