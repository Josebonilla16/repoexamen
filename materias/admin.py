from django.contrib import admin
from materias.models import  Materia, MateriaAdmin, Grado, GradoAdmin
# Register your models here.
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grado, GradoAdmin)
