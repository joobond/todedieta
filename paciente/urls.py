from django.conf.urls import url
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^$',views.dadosPaciente, name="pacientes"),
    url(r'^cadastrar/',views.cadastrarPaciente, name="cadastrar_paciente"),
    url(r'^formulario-paciente/',views.pacienteFormulario, name="formulario_paciente"),
]