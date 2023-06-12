from django.contrib import admin
from .models import Suministro, Folio, SerieVales
# Register your models here.
admin.site.register(Suministro)
admin.site.register(Folio)
admin.site.register(SerieVales)