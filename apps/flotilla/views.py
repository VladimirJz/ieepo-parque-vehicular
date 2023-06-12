from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Marca,Modelo,Vehiculo
from .serializers import MarcaSerializer,ModeloSerializer,VehiculoSerializer
from rest_framework import permissions

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
    permission_classes = (permissions.IsAuthenticated,)

class VehiculoViewSet(ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = (permissions.IsAuthenticated,)