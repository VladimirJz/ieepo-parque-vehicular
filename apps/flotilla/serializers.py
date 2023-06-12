from rest_framework import serializers
from .models import Marca,Modelo,Vehiculo

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__' 

class ModeloSerializer(serializers.ModelSerializer):
    Marca = serializers.PrimaryKeyRelatedField(queryset= Marca.objects.all(),many=False)
    MarcaNombre=serializers.CharField(source='Marca.Nombre',read_only=True)
    
    class Meta:
        model = Modelo
        fields = '__all__' 


class VehiculoSerializer(serializers.ModelSerializer):
    Modelo = serializers.PrimaryKeyRelatedField(queryset= Modelo.objects.all(),many=False)
    
    class Meta:
        model = Vehiculo
        fields = '__all__' 
