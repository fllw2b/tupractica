from django.urls import path
from . import views
from apps.usuarios import views as usuario_views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-comunas/<int:region_id>/',
         usuario_views.get_comunas, name='get_comunas'),
]
