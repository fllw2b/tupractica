from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.db import transaction
from ...models import Usuario, Estudiante, Region, Comuna, Carrera
from ....anuncios.models import AnuncioPractica, Postulacion
from ...serializers.estudiante_serializer import EstudianteSerializer
from ....anuncios.serializers.anuncio_serializers import AnuncioPracticaSerializer
from ....anuncios.serializers.postulacion_serializers import PostulacionSerializer

# registro estudiante
class RegistroEstudianteAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        try:
            with transaction.atomic():
                usuario = Usuario.objects.create_user(
                    email=data["email"],
                    password=data["password"],
                    es_estudiante=True
                )
                estudiante = Estudiante.objects.create(
                    usuario=usuario,
                    nombres=data["nombres"],
                    apellidos=data["apellidos"],
                    rut=data["rut"],
                    region=Region.objects.get(id=data["region_id"]),
                    comuna=Comuna.objects.get(id=data["comuna_id"]),
                    carrera=Carrera.objects.get(id=data["carrera_id"]),
                    fecha_nacimiento=data["fecha_nacimiento"],
                    genero=data["genero"],
                    direccion=data["direccion"],
                    telefono=data["telefono"]
                )
                serializer = EstudianteSerializer(estudiante)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Region.DoesNotExist:
            return Response({"error": "La región especificada no existe."}, status=status.HTTP_400_BAD_REQUEST)
        except Comuna.DoesNotExist:
            return Response({"error": "La comuna especificada no existe."}, status=status.HTTP_400_BAD_REQUEST)
        except Carrera.DoesNotExist:
            return Response({"error": "La carrera especificada no existe."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# detalle estudiante
class EstudianteDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            estudiante = request.user.estudiante
            serializer = EstudianteSerializer(estudiante)
            return Response(serializer.data)
        except Estudiante.DoesNotExist:
            return Response({'error': 'No se encontró el perfil del estudiante.'}, status=404)

class ListPracticasAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        practicas = AnuncioPractica.objects.all()  # se obtienen todos los anuncios de practica
        serializer = AnuncioPracticaSerializer(practicas, many=True)
        return Response(serializer.data, status=200)

# modificar perfil estudiante
class UpdateEstudianteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        estudiante = request.user.estudiante
        serializer = EstudianteSerializer(estudiante, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  postular a un anuncio
class CreatePostulacionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        estudiante = request.user.estudiante
        anuncio_id = request.data.get("anuncio_id")

        if not anuncio_id:
            return Response({"error": "El campo 'anuncio_id' es obligatorio."}, status=400)

        try:
            anuncio = AnuncioPractica.objects.get(id=anuncio_id)
            postulacion, created = Postulacion.objects.get_or_create(estudiante=estudiante, anuncio=anuncio)

            if not created:
                return Response({"error": "Ya estás postulado a este anuncio."}, status=400)

            serializer = PostulacionSerializer(postulacion)
            return Response(serializer.data, status=201)
        except AnuncioPractica.DoesNotExist:
            return Response({"error": "El anuncio especificado no existe."}, status=404)

class HistorialPostulacionesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        estudiante = request.user.estudiante
        postulaciones = Postulacion.objects.filter(estudiante=estudiante)
        serializer = PostulacionSerializer(postulaciones, many=True)
        return Response(serializer.data, status=200)
    

class DeletePostulacionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, postulacion_id):
        estudiante = request.user.estudiante
        try:
            postulacion = Postulacion.objects.get(id=postulacion_id, estudiante=estudiante)
            postulacion.delete()
            return Response({"detail": "Postulación eliminada con éxito."}, status=204)
        except Postulacion.DoesNotExist:
            return Response({"error": "La postulación no existe o no pertenece al estudiante."}, status=404)
        
class DetallePracticaAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, practica_id):
        try:
            practica = AnuncioPractica.objects.get(id=practica_id)
            serializer = AnuncioPracticaSerializer(practica)
            return Response(serializer.data, status=200)
        except AnuncioPractica.DoesNotExist:
            return Response({"error": "La práctica especificada no existe."}, status=404)

class ListRegionesAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        regiones = Region.objects.all().values('id', 'nombre')
        return Response(list(regiones))
    
class ListComunasByRegionAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, region_id):
        comunas = Comuna.objects.filter(region_id=region_id).values('id', 'nombre')
        return Response(list(comunas))

class ListCarrerasAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        carreras = Carrera.objects.all().values('id', 'nombre')
        return Response(list(carreras))
