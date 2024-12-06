from django.urls import path
from . import views
from .api_views.api.estudiante_views import ListPracticasAPIView, CreatePostulacionAPIView, EstudianteDetailView, UpdateEstudianteAPIView, HistorialPostulacionesAPIView, DeletePostulacionAPIView, DetallePracticaAPIView, ListCarrerasAPIView, ListComunasByRegionAPIView, ListRegionesAPIView, AnuncioPracticasMatchView, VerificarPostulacionView
from .api_views.api.estudiante_views import RegistroEstudianteAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import perfil_empresa, perfil_publico_empresa, editar_perfil_empresa


urlpatterns = [
     #     path('login/', views.login, name='login'),
     path('get-comunas/<int:region_id>/', views.get_comunas, name='get_comunas'),
     path('seleccionar-tipo/', views.seleccionar_tipo_usuario,
          name='seleccionar_tipo_usuario'),
     path('registro-estudiante/', views.registro_estudiante,
          name='registro_estudiante'),
     path('registro-empresa/', views.registro_empresa, name='registro_empresa'),
     path('login/', views.iniciar_sesion, name='login'),
     path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
     path('perfil/estudiante/<int:estudiante_id>/', views.perfil_estudiante, name='perfil_publico_estudiante'),
     path('perfil/estudiante/', views.perfil_estudiante, name='perfil_estudiante'),
     path('perfil/empresa/', views.perfil_empresa, name='perfil_empresa'),
     path('empresa/<int:empresa_id>/', perfil_publico_empresa, name='perfil_publico_empresa'),
     path('perfil/empresa/editar/', views.editar_perfil_empresa, name='editar_perfil_empresa'),


     
     # urls de la API
     path('api/registro/estudiante/', RegistroEstudianteAPIView.as_view(), name='api_registro_estudiante'),
     path('api/login/', TokenObtainPairView.as_view(), name='api_login'),
     path('api/token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
     path('api/practicas/', ListPracticasAPIView.as_view(), name='list_practicas'),
     path('api/postulacion/', CreatePostulacionAPIView.as_view(), name='create_postulacion'),
     path('api/estudiante/detail/', EstudianteDetailView.as_view(), name='api_estudiante_detail'),
     path('api/estudiante/update/', UpdateEstudianteAPIView.as_view(), name='api_estudiante_update'),
     path('api/postulaciones/', HistorialPostulacionesAPIView.as_view(), name='historial_postulaciones'),
     path('api/postulacion/<int:postulacion_id>/', DeletePostulacionAPIView.as_view(), name='delete_postulacion'),
     path('api/practicas/<int:pk>/', DetallePracticaAPIView.as_view(), name='detalle_practica'),
     path('api/regiones/', ListRegionesAPIView.as_view(), name='list_regiones'),
     path('api/get-comunas/<int:region_id>/', ListComunasByRegionAPIView.as_view(), name='list_comunas'),
     path('api/carreras/', ListCarrerasAPIView.as_view(), name='list_carreras'),
     path('anuncios/match/', AnuncioPracticasMatchView.as_view(), name='anuncios-match'),
     path('api/verificar_postulacion/<int:anuncio_id>/', VerificarPostulacionView.as_view(), name='verificar-postulacion'),
]


