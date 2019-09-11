from django.conf.urls import url
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^$',views.dadosPaciente),
    url(r'^cadastrar/',views.cadastrarPaciente),
    url(r'^formulario-paciente/',views.pacienteFormulario),
]