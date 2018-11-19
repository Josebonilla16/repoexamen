from django.contrib import messages
from .forms import GradoForm
from django.shortcuts import render
from django.contrib import messages
from materias.models import Grado, Materia, Detalle

def materia_nuevo (request):
    if request.method == "POST":
        formulario = GradoForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(grado=formulario.cleaned_data['grado'], seccion=formulario.cleaned_data['seccion'])
            for materia_id in request.POST.getlist('materias'):
                detalle = Detalle(materia_id=materia_id, grado_id = grado.id)
                detalle.save()
            messages.add_message(request, messages.SUCCESS, 'Materias asignadas exitosamente')
    else:
        formulario = GradoForm()
    return render(request, 'materias/materia_editar.html', {'formulario': formulario})
