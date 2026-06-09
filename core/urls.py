from django.urls import path
from . import views


urlpatterns = [

    # HOME
    path(
        '',
        views.home,
        name='home'
    ),

    # ALUNOS
    path(
        'alunos/',
        views.listar_alunos,
        name='alunos'
    ),

    path(
        'editar-aluno/<int:aluno_id>/',
        views.editar_aluno,
        name='editar_aluno'
    ),

    path(
        'excluir-aluno/<int:aluno_id>/',
        views.excluir_aluno,
        name='excluir_aluno'
    ),

    # DISCIPLINAS
    path(
        'disciplinas/',
        views.listar_disciplinas,
        name='disciplinas'
    ),

    path(
        'editar-disciplina/<int:disciplina_id>/',
        views.editar_disciplina,
        name='editar_disciplina'
    ),

    path(
        'excluir-disciplina/<int:disciplina_id>/',
        views.excluir_disciplina,
        name='excluir_disciplina'
    ),

    # TURMAS
    path(
        'turmas/',
        views.listar_turmas,
        name='turmas'
    ),

    path(
        'editar-turma/<int:turma_id>/',
        views.editar_turma,
        name='editar_turma'
    ),

    path(
        'excluir-turma/<int:turma_id>/',
        views.excluir_turma,
        name='excluir_turma'
    ),

    # MATRICULAS
    path(
        'matriculas/',
        views.listar_matriculas,
        name='matriculas'
    ),

    path(
        'editar-matricula/<int:matricula_id>/',
        views.editar_matricula,
        name='editar_matricula'
    ),

    path(
        'cancelar-matricula/<int:matricula_id>/',
        views.cancelar_matricula,
        name='cancelar_matricula'
    ),

    path(
        'excluir-matricula/<int:matricula_id>/',
        views.excluir_matricula,
        name='excluir_matricula'
    ),

]