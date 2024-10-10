from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_anuncio, name='crear_anuncio'),
    path('listar/', views.listar_anuncios, name='listar_anuncios'),
    path('modificar/<int:anuncio_id>/',
         views.modificar_anuncio, name='modificar_anuncio'),
    path('eliminar/<int:anuncio_id>/',
         views.eliminar_anuncio, name='eliminar_anuncio'),
]
