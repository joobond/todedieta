from django.conf.urls import url
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^$',views.dadosAlimento, name="alimentos"),
    url(r'^cadastrar/',views.cadastrarAlimento, name="cadastrar_alimento"),
    url(r'^formulario-alimento/',views.alimentoFormulario, name="formulario_alimento"),
]