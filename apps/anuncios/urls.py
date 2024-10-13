from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_anuncio, name='crear_anuncio'),
    path('mis-anuncios/', views.mis_anuncios, name='mis_anuncios'),
    path('modificar/<int:anuncio_id>/',
         views.modificar_anuncio, name='modificar_anuncio'),
    path('anuncios/<int:anuncio_id>/',
         views.eliminar_anuncio, name='eliminar_anuncio'),
    path('', views.lista_anuncios, name='lista_anuncios'),
    path('<int:anuncio_id>/', views.detalle_anuncio, name='detalle_anuncio'),
    path('postular/<int:anuncio_id>/',
         views.postular_anuncio, name='postular_anuncio'),
    path('historial_postulaciones/', views.historial_postulaciones,
         name='historial_postulaciones'),
    path('postulaciones_empresa/', views.postulaciones_empresa,
         name='postulaciones_empresa'),
]
