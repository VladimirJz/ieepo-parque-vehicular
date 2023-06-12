from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet,ModeloViewSet,VehiculoViewSet


router = DefaultRouter()
router.register(r'marca', MarcaViewSet, basename='vehiculo-marca')
router.register(r'modelo', ModeloViewSet, basename='vehiculo-modelo')
router.register(r'vehiculo', VehiculoViewSet, basename='vehiculo')
urlpatterns = [
    path('flota/', include(router.urls)),
   
]