from django.db import models

# Create your models here.
class Marca(models.Model):
    Nombre=models.CharField(max_length=30)
    Clave=models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.Nombre 

class Modelo(models.Model):
    Marca=models.ForeignKey(Marca,on_delete=models.SET_DEFAULT,default=1)
    Nombre=models.CharField(max_length=30)
    Clave=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.Marca.Nombre + ' ' +f'{self.Nombre}'


class Vehiculo(models.Model):
    Modelo=models.ForeignKey(Modelo,on_delete=models.SET_NULL,null=True,blank=True)
    Anio =models.SmallIntegerField(default=0)
    Color=models.CharField(max_length=20)
    Placas=models.CharField(max_length=20)
    Serie=models.CharField(max_length=50)
    Alias=models.CharField(max_length=50)
    Notas=models.TextField(blank=True)
        
    def __str__(self) -> str:
        return self.Alias + f'({self.Modelo})'
    



class Area(models.Model):
    Nombre=models.CharField(max_length=50)
    # direccion #responsable ...etc 
    def __str__(self) -> str:
        return self.Nombre

class Departamento(models.Model):
    Area=models.ForeignKey(Area, on_delete=models.SET_NULL,null=True)
    Nombre=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.Nombre + f'({self.Area})' 

class Conductor(models.Model):
    Nombre=models.CharField(max_length=50)
    Apellidos=models.CharField(max_length=200)
    Departamento=models.ForeignKey(Departamento,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return  self.Apellidos + ' '+  self.Nombre 






