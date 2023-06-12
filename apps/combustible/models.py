from django.db import models
from apps.flotilla.models import Conductor,Vehiculo

# Create your models here.
class SerieVales(models.Model):
    Serie=models.CharField(max_length=20,primary_key=True)
    FolioInicial=models.SmallIntegerField()
    FolioFinal=models.SmallIntegerField()
    FolioActual=models.SmallIntegerField()
    FechaExpedicion=models.DateField()

    def __str__(self) -> str:
        return self.Serie + f' ({self.FolioInicial}-{self.FolioFinal})'


class Suministro(models.Model):
    Serie=models.ForeignKey(SerieVales,on_delete=models.SET_NULL,null=True)
    Vehiculo=models.ForeignKey(Vehiculo,on_delete=models.SET_NULL,null=True)
    Conductor=models.ForeignKey(Conductor, on_delete=models.SET_NULL,null=True)
    Recibe=models.CharField(max_length=200)
    Fecha = models.DateField()
    Litros=models.SmallIntegerField()
    
    def __str__(self) -> str:
        return f' { self.Fecha } - () {self.Serie.Serie } {self.Vehiculo}) '
    



ESTATUS_FOLIO=[(1,'Resguardo'),(2,'Entregado'),(3,'Aplicado'),(4,'Cancelado')]
class Folio(models.Model):
    Numero=models.IntegerField()
    Suministro=models.ForeignKey(Suministro,on_delete=models.SET_NULL,null=True)
    #Serie_id=models.ForeignKey(SerieVales, on_delete=models.SET_NULL,null=True)
    Litros=models.SmallIntegerField()
    Estatus=models.SmallIntegerField(choices=ESTATUS_FOLIO,default=1)

    
    def __str__(self) -> str:
        return f' {self.Suministro.Serie.Serie } - { self.Numero } '
    



