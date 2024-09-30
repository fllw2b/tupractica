from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('get-comunas/<int:region_id>/', views.get_comunas, name='get_comunas'),
    path('seleccionar-tipo/', views.seleccionar_tipo_usuario,
         name='seleccionar_tipo_usuario'),
    path('registro-estudiante/', views.registro_estudiante,
         name='registro_estudiante'),
    path('registro-empresa/', views.registro_empresa, name='registro_empresa'),
]
