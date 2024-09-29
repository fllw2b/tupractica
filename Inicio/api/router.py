from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    
    path('USUARIO/',usuario_api_view, name= 'usuario api'),
    path('USUARIO/<int:pk>/',usuario_detail_view, name = 'usuario api detalle' ),
    path('USUARIOC/<str:nombreusuario>/<str:contrasena>/', usuarioc, name='usuario_contrasena'),

    path('REGION/',region_api_view, name= 'region api'),
    path('REGION/<int:pk>/',region_detail_view, name = 'region api detalle' ),
    
    path('PROVINCIA/',provincia_api_view, name= 'provincia api'),
    path('PROVINCIA/<int:pk>/',provincia_detail_view, name = 'provincia api detalle' ),
    
    path('COMUNA/',comuna_api_view, name= 'comuna api'),
    path('COMUNA/<int:pk>/',comuna_detail_view, name = 'comuna api detalle' ),
    
    path('EMPRESA/',empresa_api_view, name= 'empresa api'),
    path('EMPRESA/<int:pk>/',empresa_detail_view, name = 'empresa api detalle' ),
    path('EMPRESAC/<int:pk>/<str:contrasena>/', empresac, name='empresa_contrasena'),

    path('ANUNCIO/',anuncio_api_view, name= 'anuncio api'),
    path('ANUNCIO/<int:pk>/',anuncio_detail_view, name = 'anuncio api detalle' ),
]


# from rest_framework.routers import DefaultRouter

# router_posts = DefaultRouter()

# router_posts.register(prefix='USUARIO',basename='USUARIO',viewset=USUARIOApiViewSet)
# router_posts.register(prefix='REGION',basename='REGION',viewset=REGIONViewSet)
# router_posts.register(prefix='PROVINCIA',basename='PROVINCIA',viewset=PROVINCIAViewSet)
# router_posts.register(prefix='COMUNA',basename='COMUNA',viewset=COMUNAViewSet)
# router_posts.register(prefix='CLIENTE',basename='CLIENTE',viewset=CLIENTEViewSet)
# router_posts.register(prefix='SUCURSAL',basename='SUCURSAL',viewset=SUCURSALViewSet)
# router_posts.register(prefix='CATEGORIA',basename='CATEGORIA',viewset=CATEGORIAViewSet)
# router_posts.register(prefix='PROVEEDOR',basename='PROVEEDOR',viewset=PROVEEDORViewSet)
# router_posts.register(prefix='PRODUCTO',basename='PRODUCTO',viewset=PRODUCTOViewSet)
# router_posts.register(prefix='TIPO_EMPLEADO',basename='TIPO_EMPLEADO',viewset=TIPO_EMPLEADOViewSet)
# router_posts.register(prefix='EMPLEADO',basename='EMPLEADO',viewset=EMPLEADOViewSet)
# router_posts.register(prefix='VENTA',basename='VENTA',viewset=VENTAViewSet)
# router_posts.register(prefix='TIPOEMISION',basename='TIPOEMISION',viewset=TIPOEMISIONViewSet)
# router_posts.register(prefix='VENTA_DETALLE',basename='VENTA_DETALLE',viewset=VENTA_DETALLEViewSet)
# router_posts.register(prefix='COURRIER',basename='COURRIER',viewset=COURRIERViewSet)
# router_posts.register(prefix='DESPACHO',basename='DESPACHO',viewset=DESPACHOViewSet)
# router_posts.register(prefix='BODEGA',basename='BODEGA',viewset=BODEGAViewSet)
# router_posts.register(prefix='ESPACIOS',basename='ESPACIOS',viewset=ESPACIOSViewSet)
# router_posts.register(prefix='BODEGA_DETALLE',basename='BODEGA_DETALLE',viewset=BODEGA_DETALLEViewSet)
# router_posts.register(prefix='GUIA_DESPACHO',basename='GUIA_DESPACHO',viewset=GUIA_DESPACHOViewSet)
# router_posts.register(prefix='COMPRA',basename='COMPRA',viewset=COMPRAViewSet)
# router_posts.register(prefix='COMPRA_DETALLE',basename='COMPRA_DETALLE',viewset=COMPRA_DETALLEViewSet)