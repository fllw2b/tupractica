from Inicio.models import *
from django.shortcuts import render
from Inicio.api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import bcrypt


def home(request):
    return render(request,'home.html')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def usuario_api_view(request):
    if request.method == 'GET':
        usuarios = USUARIO.objects.all()
        usuarios_serializer = USUARIOSerializer(usuarios,many = True)
        return Response(usuarios_serializer.data)
    elif request.method == 'POST':
        usuarios_serializer = USUARIOSerializer(data = request.data)
        raw_password = request.data.get('contrasena')
        hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
        request.data['contrasena'] = hashed_password.decode('utf-8')
        if usuarios_serializer.is_valid():
            usuarios_serializer.save()
            return Response(usuarios_serializer.data)
        errors = usuarios_serializer.errors
        if 'email' in errors:
            return Response({'detail': 'Email no válido.'}, status=422)
        
        return Response(usuarios_serializer.errors)
    else:
        return Response('Metodo no permitido') 

@api_view(['GET','PUT','DELETE'])
def usuario_detail_view(request,pk=None):
    if request.method == 'GET':
        usuarios = USUARIO.objects.filter(id = pk).first()
        usuarios_serializer =  USUARIOSerializer(usuarios)
        return Response(usuarios_serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
            usuario = USUARIO.objects.filter(id = pk).first()
            raw_password = request.data.get('contrasena')
            hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
            request.data['contrasena'] = hashed_password.decode('utf-8')
            usuario_serializar = USUARIOSerializer(usuario,data = request.data)
            if usuario_serializar.is_valid():
                usuario_serializar.save()
                return Response(usuario_serializar.errors)
    elif request.method == 'DELETE':
        usuario = USUARIO.objects.filter(id = pk).first()
        usuario.delete()
        return Response('Eliminado')
    else:
        return Response('Metodo no permitido')
    
@api_view(['GET'])
def usuarioc(request, nombreusuario, contrasena):
    try:
        usuario = USUARIO.objects.get(nombreusuario=nombreusuario)
        is_password_correct = bcrypt.checkpw(contrasena.encode('utf-8'), usuario.contrasena.encode('utf-8'))
        response_data = {
            'id': usuario.id,
            'nombreusuario': usuario.nombreusuario,
            'email': usuario.email,
            'contrasena': is_password_correct,
        }

        return Response(response_data, status=status.HTTP_200_OK)
    except USUARIO.DoesNotExist:
        return Response({'error': 'Usuario no encontrado.'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ------------------------------------------------------------------------
@api_view(['GET'])
def region_api_view(request):
    if request.method == 'GET':
        regiones = REGION.objects.all()
        regiones_serializer = REGIONSerializer(regiones,many = True)
        return Response(regiones_serializer.data)
    else:
        return Response('Metodo no permitido')

@api_view(['GET'])
def region_detail_view(request,pk=None):
    if request.method == 'GET':
        regiones = REGION.objects.filter(id = pk).first()
        regiones_serializer = REGIONSerializer(regiones)
        return Response(regiones_serializer.data)
    else:
        return Response('Metodo no permitido')
    
# ------------------------------------------------------------------------
@api_view(['GET'])
def provincia_api_view(request):
    if request.method == 'GET':
        provincias = PROVINCIA.objects.all()
        provincias_serializer = REGIONSerializer(provincias,many = True)
        return Response(provincias_serializer.data)
    else:
        return Response('Metodo no permitido')

@api_view(['GET'])
def provincia_detail_view(request,pk=None):
    if request.method == 'GET':
        provincias = PROVINCIA.objects.filter(id = pk).first()
        provincias_serializer = REGIONSerializer(provincias)
        return Response(provincias_serializer.data)
    else:
        return Response('Metodo no permitido')
    
# ------------------------------------------------------------------------
@api_view(['GET'])
def comuna_api_view(request):
    if request.method == 'GET':
        comunas = COMUNA.objects.all()
        comunas_serializer = COMUNASerializer(comunas,many = True)
        return Response(comunas_serializer.data)
    else:
        return Response('Metodo no permitido')
@api_view(['GET'])
def comuna_detail_view(request,pk=None):
    if request.method == 'GET':
        comunas = COMUNA.objects.filter(id = pk).first()
        comunas_serializer = COMUNASerializer(comunas)
        return Response(comunas_serializer.data)
    else:
        return Response('Metodo no permitido')

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def empresa_api_view(request):
    if request.method == 'GET':
        empresas = EMPRESA.objects.all()
        empresas_serializer = EMPRESASerializer(empresas,many = True)
        return Response(empresas_serializer.data)
    elif request.method == 'POST':
        empresas_serializer = EMPRESASerializer(data = request.data)
        if empresas_serializer.is_valid():
            empresas_serializer.save()
            return Response(empresas_serializer.data)
        return Response(empresas_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','PUT','DELETE'])
def empresa_detail_view(request,pk=None):
    if request.method == 'GET':
        empresas = EMPRESA.objects.filter(id = pk).first()
        empresas_serializer = EMPRESASerializer(empresas)
        return Response(empresas_serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
            empresas = EMPRESA.objects.filter(id = pk).first()
            empresas_serializer = EMPRESASerializer(empresa,data = request.data)
            if empresas_serializer.is_valid():
                empresas_serializer.save()
                return Response(empresas_serializer.errors)
    elif request.method == 'DELETE':
        empresa = EMPRESA.objects.filter(id = pk).first()
        empresa.delete()
        return Response('Eliminado')
    else:
        return Response('Metodo no permitido')
    
@api_view(['GET'])
def empresac(request, pk, contrasena):
    if request.method == 'GET':
        empresa = EMPRESA.objects.filter(id=pk).first()
        is_password_correct = bcrypt.checkpw(contrasena.encode('utf-8'), empresa.contrasena.encode('utf-8'))
        response_data = {
            'id': empresa.id,
            'rut': empresa.rutEmpresa,
            'nombreEmpresa': empresa.nombreEmpresa,
            'direccionEMP': empresa.direccionEMP,
            'telefonoEMP': empresa.telefonoEMP,
            'email': empresa.email,
            'id_comuna': empresa.id_comuna,
            'contrasena': is_password_correct,
        }
        return Response(response_data)
    else:
        return Response('Metodo no permitido')
    

# ------------------------------------------------------------------------
@api_view(['GET','POST'])
def anuncio_api_view(request):
    if request.method == 'GET':
        anuncios = ANUNCIO.objects.all()
        anuncios_serializer = ANUNCIOSerializer(anuncios,many = True)
        return Response(anuncios_serializer.data)
    elif request.method == 'POST':
        anuncios_serializer = anuncios_serializer(data = request.data)
        if anuncios_serializer.is_valid():
            anuncios_serializer.save()
            return Response(anuncios_serializer.data)
        return Response(anuncios_serializer.errors)
    else:
        return Response('Metodo no permitido') 
@api_view(['GET','PUT','DELETE'])
def anuncio_detail_view(request,pk=None):
    if request.method == 'GET':
        anuncios = ANUNCIO.objects.filter(id = pk).first()
        anuncios_serializer = anuncios_serializer(anuncios)
        return Response(anuncios_serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
            anuncio = ANUNCIO.objects.filter(id = pk).first()
            anuncio_serializar = anuncios_serializer(anuncio,data = request.data)
            if anuncio_serializar.is_valid():
                anuncio_serializar.save()
                return Response(anuncio_serializar.errors)
    elif request.method == 'DELETE':
        anuncio = ANUNCIO.objects.filter(id = pk).first()
        anuncio.delete()
        return Response('Eliminado')
    else:
        return Response('Metodo no permitido')


# ------------------------------------------------------------------------

# from rest_framework.viewsets import ModelViewSet

# class USUARIOApiViewSet(ModelViewSet):
#     serializer_class=USUARIOSerializer
#     queryset=USUARIO.objects.all()

# class REGIONViewSet(ModelViewSet):
#     serializer_class=REGIONSerializer
#     queryset=REGION.objects.all()
    
# class PROVINCIAViewSet(ModelViewSet):
#     serializer_class=PROVINCIASerializer
#     queryset=PROVINCIA.objects.all()
    
# class COMUNAViewSet(ModelViewSet):
#     serializer_class=COMUNASerializer
#     queryset=COMUNA.objects.all()
    
# class CLIENTEViewSet(ModelViewSet):
#     serializer_class=CLIENTESerializer
#     queryset=CLIENTE.objects.all()
    
# class SUCURSALViewSet(ModelViewSet):
#     serializer_class=SUCURSALSerializer
#     queryset=SUCURSAL.objects.all()
    
# class CATEGORIAViewSet(ModelViewSet):
#     serializer_class=CATEGORIASerializer
#     queryset=CATEGORIA.objects.all()
    
# class PROVEEDORViewSet(ModelViewSet):
#     serializer_class=PROVEEDORSerializer
#     queryset=PROVEEDOR.objects.all()
    
# class PRODUCTOViewSet(ModelViewSet):
#     serializer_class=PRODUCTOSerializer
#     queryset=PRODUCTO.objects.all()
    
# class TIPO_EMPLEADOViewSet(ModelViewSet):
#     serializer_class=TIPO_EMPLEADOSerializer
#     queryset=TIPO_EMPLEADO.objects.all()
    
# class EMPLEADOViewSet(ModelViewSet):
#     serializer_class=EMPLEADOSerializer
#     queryset=EMPLEADO.objects.all()
    
# class VENTAViewSet(ModelViewSet):
#     serializer_class=VENTASerializer
#     queryset=VENTA.objects.all()

# class TIPOEMISIONViewSet(ModelViewSet):
#     serializer_class=TIPOEMISIONSerializer
#     queryset=TIPOEMISION.objects.all()
    
# class VENTA_DETALLEViewSet(ModelViewSet):
#     serializer_class=VENTA_DETALLESerializer
#     queryset=VENTA_DETALLE.objects.all()
    
# class COURRIERViewSet(ModelViewSet):
#     serializer_class=COURRIERSerializer
#     queryset=COURRIER.objects.all()
    
# class DESPACHOViewSet(ModelViewSet):
#     serializer_class=DESPACHOSerializer
#     queryset=DESPACHO.objects.all()
    
# class BODEGAViewSet(ModelViewSet):
#     serializer_class=BODEGASerializer
#     queryset=BODEGA.objects.all()
    
# class ESPACIOSViewSet(ModelViewSet):
#     serializer_class=ESPACIOSSerializer
#     queryset=ESPACIOS.objects.all()
    
# class BODEGA_DETALLEViewSet(ModelViewSet):
#     serializer_class=BODEGA_DETALLESerializer
#     queryset=BODEGA_DETALLE.objects.all()
    
# class GUIA_DESPACHOViewSet(ModelViewSet):
#     serializer_class=GUIA_DESPACHOSerializer
#     queryset=GUIA_DESPACHO.objects.all()
    
# class COMPRAViewSet(ModelViewSet):
#     serializer_class=COMPRASerializer
#     queryset=COMPRA.objects.all()
    
# class COMPRA_DETALLEViewSet(ModelViewSet):
#     serializer_class=COMPRA_DETALLESerializer
#     queryset=COMPRA_DETALLE.objects.all()