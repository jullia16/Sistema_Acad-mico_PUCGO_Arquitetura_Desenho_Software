from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path(
        'alunos/',
        views.listar_alunos,
        name='alunos'
    ),

    path(
        'disciplinas/',
        views.listar_disciplinas,
        name='disciplinas'
    ),

    path(
        'turmas/',
        views.listar_turmas,
        name='turmas'
    ),

    path(
        'matriculas/',
        views.listar_matriculas,
        name='matriculas'
    ),

    path(
    'cancelar-matricula/<int:matricula_id>/',
    views.cancelar_matricula,
    name='cancelar_matricula'
    ),

    path(
    'editar-matricula/<int:matricula_id>/',
    views.editar_matricula,
    name='editar_matricula'
    ),

path(
    'excluir-matricula/<int:matricula_id>/',
    views.excluir_matricula,
    name='excluir_matricula'
    ),
]