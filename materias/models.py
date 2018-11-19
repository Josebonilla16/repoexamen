from django.db import models
from django.contrib import admin

class Materia(models.Model):
    nombre  =   models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Grado(models.Model):
    grado  =   models.CharField(max_length=200)
    seccion =   models.CharField(max_length=200)
    materias   = models.ManyToManyField(Materia, through='Detalle')
    def __str__(self):
        return self.grado

class Detalle (models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

class DetalleInLine(admin.TabularInline):
    model = Detalle
    extra = 1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (DetalleInLine,)

class GradoAdmin (admin.ModelAdmin):
    inlines = (DetalleInLine,)
