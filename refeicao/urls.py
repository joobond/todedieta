from django.conf.urls import url
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^$',views.dadosRefeicao, name="refeicoes"),
    url(r'^cadastrar/',views.cadastrarRefeicao, name="cadastrar_refeicao"),
    url(r'^formulario-refeicao/',views.refeicaoFormulario, name="formulario_refeicao"),
    url(r'^busca-alimento/$', views.autocomplete, name="buscaAlimentos"),
]