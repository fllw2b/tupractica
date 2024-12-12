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

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

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
        'tags': tags,
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


# @login_required
# def mis_anuncios2(request):
#     if request.user.is_authenticated and hasattr(request.user, 'empresa'):
#         empresa = request.user.empresa
#         anuncios = AnuncioPractica.objects.filter(empresa=empresa)
#         return render(request, 'empresas/mis_anuncios.html', {'anuncios': anuncios})
#     else:
#         return redirect('login')

def listar_anuncios(request):
    anuncios = AnuncioPractica.objects.all()
    busqueda = request.GET.get('busqueda', '')
    region = request.GET.get('region', '')
    modalidad = request.GET.get('modalidad', '')

    if busqueda:
        anuncios = anuncios.filter(titulo__icontains=busqueda)
    
    if region:
        anuncios = anuncios.filter(region__nombre=region)
    
    if modalidad:
        anuncios = anuncios.filter(modalidad__iexact=modalidad)

    recomendaciones = []

    # vemos si el user es estudiante y si ya postulo al anuncio
    if hasattr(request.user, 'estudiante'):
        estudiante = request.user.estudiante
        habilidades_estudiante = set(estudiante.habilidades.all())

        for anuncio in anuncios:
            # calculamos %
            requisitos_anuncio = set(anuncio.requisitos.all())
            habilidades_comunes = habilidades_estudiante.intersection(requisitos_anuncio)
            total_requisitos = len(requisitos_anuncio)
            if total_requisitos > 0:
                porcentaje_coincidencia = int((len(habilidades_comunes) / total_requisitos) * 100)
            else:
                porcentaje_coincidencia = 0

            # vemos si ya postulo
            ya_postulo = Postulacion.objects.filter(estudiante=estudiante, anuncio=anuncio).exists()

            recomendaciones.append({
                'anuncio': anuncio,
                'porcentaje_coincidencia': porcentaje_coincidencia,
                'ya_postulo': ya_postulo
            })

        # ordenamos por % de mayor a menor
        recomendaciones.sort(key=lambda x: x['porcentaje_coincidencia'], reverse=True)
    else:
        # si no es estudiante, mostrar los anuncios sin el porcentaje
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
        # Crear la postulación
        Postulacion.objects.create(estudiante=estudiante, anuncio=anuncio)

        # Enviar correo de confirmación al estudiante
        enviar_notificacion_postulacion(estudiante, anuncio, 'En revisión')

        messages.success(request, "Postulación realizada exitosamente. Se ha enviado un correo de confirmación.")

    return redirect('listar_anuncios')

@login_required
def historial_postulaciones(request):
    if not hasattr(request.user, 'estudiante'):
        messages.error(request, "Solo los estudiantes pueden ver su historial de postulaciones.")
        return redirect('lista_anuncios')

    postulaciones = Postulacion.objects.filter(estudiante=request.user.estudiante).select_related('anuncio')
    
    return render(request, 'estudiantes/historial_postulaciones.html', {'postulaciones': postulaciones})

@login_required
def mis_anuncios(request):
    if not hasattr(request.user, 'empresa'):
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('home')

    empresa = request.user.empresa
    anuncios = AnuncioPractica.objects.filter(empresa=empresa)

    # Filtros
    busqueda = request.GET.get('busqueda', '')
    modalidad = request.GET.get('modalidad', '')
    region_id = request.GET.get('region', '')

    if busqueda:
        anuncios = anuncios.filter(titulo__icontains=busqueda)

    if modalidad:
        anuncios = anuncios.filter(modalidad=modalidad)

    if region_id:
        anuncios = anuncios.filter(region_id=region_id)

    regiones = Region.objects.all()

    return render(request, 'empresas/mis_anuncios.html', {
        'anuncios': anuncios,
        'regiones': regiones,
    })


@login_required
def postulantes(request, anuncio_id):
    anuncio = get_object_or_404(AnuncioPractica, id=anuncio_id)

    # obtenemos todos los q postularon al anuncio
    postulantes = Postulacion.objects.filter(anuncio=anuncio)

    # filtros
    carrera = request.GET.get('carrera', '')
    region_id = request.GET.get('region', '')
    cv = request.GET.get('cv', '')
    estado = request.GET.get('estado', '')

    if carrera:
        postulantes = postulantes.filter(estudiante__carrera__icontains=carrera)

    if region_id:
        postulantes = postulantes.filter(estudiante__region__id=region_id)

    if cv:
        if cv == '1':
            postulantes = postulantes.filter(estudiante__cv__isnull=False)
        elif cv == '0':
            postulantes = postulantes.filter(estudiante__cv__isnull=True)

    if estado:
        postulantes = postulantes.filter(estado=estado)

    # calculamos el % de compatibilidad
    for postulacion in postulantes:
        requisitos_anuncio = set(anuncio.requisitos.all())
        habilidades_estudiante = set(postulacion.estudiante.habilidades.all())
        coincidencia = len(requisitos_anuncio.intersection(habilidades_estudiante))
        total_requisitos = len(requisitos_anuncio)
        postulacion.compatibilidad = (
            int((coincidencia / total_requisitos) * 100) if total_requisitos > 0 else 0
        )

    # las regiones
    regiones = Region.objects.all()

    return render(request, 'empresas/postulantes.html', {
        'anuncio': anuncio,
        'postulantes': postulantes,
        'regiones': regiones,
    })

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
    porcentaje_coincidencia = None
    habilidades_estudiante = []

    # verificamos q sea estudiante
    if hasattr(request.user, 'estudiante'):
        habilidades_estudiante = list(request.user.estudiante.habilidades.all())
        estudiante = request.user.estudiante
        habilidades_estudiante = set(estudiante.habilidades.all())
        requisitos_anuncio = set(anuncio.requisitos.all())
        habilidades_comunes = habilidades_estudiante.intersection(requisitos_anuncio)
        total_requisitos = len(requisitos_anuncio)

        if total_requisitos > 0:
            porcentaje_coincidencia = int((len(habilidades_comunes) / total_requisitos) * 100)
        else:
            porcentaje_coincidencia = 0

    return render(request, 'anuncios/detalle_anuncio_ajax.html', {
        'anuncio': anuncio,
        'porcentaje_coincidencia': porcentaje_coincidencia,
        'habilidades_estudiante': habilidades_estudiante,
    })


@login_required
def eliminar_postulacion(request, postulacion_id):
    if request.method == 'POST':
        try:
            print(f"Intentando eliminar la postulación con ID: {postulacion_id}")
            postulacion = get_object_or_404(Postulacion, id=postulacion_id, estudiante=request.user.estudiante)
            postulacion.delete()
            messages.success(request, "Postulación cancelada exitosamente.")
        except Exception as e:
            messages.error(request, "Ocurrió un error al intentar cancelar la postulación.")
            print(e)  # imprimimos el error
    return redirect('historial_postulaciones')

@login_required
def cambiar_estado_postulacion(request, postulacion_id, estado):
    if not hasattr(request.user, 'empresa'):
        messages.error(request, "No tienes permiso para realizar esta acción.")
        return redirect('home')

    postulacion = get_object_or_404(Postulacion, id=postulacion_id, anuncio__empresa=request.user.empresa)

    if estado not in ['Aprobado', 'Rechazado']:
        messages.error(request, "Estado inválido.")
        return redirect('postulantes', anuncio_id=postulacion.anuncio.id)  

    postulacion.estado = estado
    postulacion.save()

    # llamamos a la funcion q hicimos directamente en el modelo
    postulacion.enviar_correo_estado()

    messages.success(request, "Postulación marcada como "+estado+" Se notificó al estudiante.")
    
    return redirect('postulantes', anuncio_id=postulacion.anuncio.id)

def enviar_notificacion_postulacion(estudiante, anuncio, estado):
    subject = "Estado de tu postulación"
    from_email = "tupractica27@gmail.com"
    to_email = estudiante.usuario.email

    # renderizamos el html con los datos
    html_content = render_to_string('anuncios/notificacion_postulacion.html', {
        'estudiante': estudiante,
        'anuncio': anuncio,
        'estado': estado,
        'url_postulaciones': 'http://tupractica.com/postulaciones',
        'year': 2024,
    })

    # creamos y enviamos el correo
    email = EmailMultiAlternatives(subject, "", from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()
