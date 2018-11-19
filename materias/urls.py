from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^materias/nuevo/$', views.materia_nuevo, name='materia_nuevo'),
    ]
