from django.shortcuts import render, redirect
from .models import Aluno, Disciplina, Turma, Matricula

from .commands.efetuar_matricula import (
    EfetuarMatriculaCommand
)

from .commands.cancelar_matricula import (
    CancelarMatriculaCommand
)


# ==================================================
# HOME
# ==================================================

def home(request):

    return render(
        request,
        'home.html'
    )


# ==================================================
# ALUNOS
# ==================================================

def listar_alunos(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')

        matricula = request.POST.get(
            'matricula'
        )

        Aluno.objects.create(
            nome=nome,
            matricula=matricula
        )

        return redirect('/alunos/')

    alunos = Aluno.objects.all()

    return render(
        request,
        'alunos.html',
        {'alunos': alunos}
    )


def editar_aluno(request, aluno_id):

    aluno = Aluno.objects.get(
        id=aluno_id
    )

    if request.method == 'POST':

        aluno.nome = request.POST.get(
            'nome'
        )

        aluno.matricula = request.POST.get(
            'matricula'
        )

        aluno.save()

        return redirect('/alunos/')

    return render(
        request,
        'editar_aluno.html',
        {'aluno': aluno}
    )


def excluir_aluno(request, aluno_id):

    aluno = Aluno.objects.get(
        id=aluno_id
    )

    aluno.delete()

    return redirect('/alunos/')


# ==================================================
# DISCIPLINAS
# ==================================================

def listar_disciplinas(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')

        codigo = request.POST.get(
            'codigo'
        )

        carga_horaria = request.POST.get(
            'carga_horaria'
        )

        Disciplina.objects.create(
            nome=nome,
            codigo=codigo,
            carga_horaria=carga_horaria
        )

        return redirect('/disciplinas/')

    disciplinas = Disciplina.objects.all()

    return render(
        request,
        'disciplinas.html',
        {'disciplinas': disciplinas}
    )


def editar_disciplina(
    request,
    disciplina_id
):

    disciplina = Disciplina.objects.get(
        id=disciplina_id
    )

    if request.method == 'POST':

        disciplina.nome = request.POST.get(
            'nome'
        )

        disciplina.codigo = request.POST.get(
            'codigo'
        )

        disciplina.carga_horaria = request.POST.get(
            'carga_horaria'
        )

        disciplina.save()

        return redirect('/disciplinas/')

    return render(
        request,
        'editar_disciplina.html',
        {'disciplina': disciplina}
    )


def excluir_disciplina(
    request,
    disciplina_id
):

    disciplina = Disciplina.objects.get(
        id=disciplina_id
    )

    disciplina.delete()

    return redirect('/disciplinas/')


# ==================================================
# TURMAS
# ==================================================

def listar_turmas(request):

    if request.method == 'POST':

        disciplina_id = request.POST.get(
            'disciplina'
        )

        semestre = request.POST.get(
            'semestre'
        )

        vagas = request.POST.get(
            'vagas'
        )

        disciplina = Disciplina.objects.get(
            id=disciplina_id
        )

        Turma.objects.create(
            disciplina=disciplina,
            semestre=semestre,
            vagas=vagas
        )

        return redirect('/turmas/')

    turmas = Turma.objects.all()

    disciplinas = Disciplina.objects.all()

    return render(
        request,
        'turmas.html',
        {
            'turmas': turmas,
            'disciplinas': disciplinas
        }
    )


def editar_turma(request, turma_id):

    turma = Turma.objects.get(
        id=turma_id
    )

    disciplinas = Disciplina.objects.all()

    if request.method == 'POST':

        disciplina_id = request.POST.get(
            'disciplina'
        )

        turma.disciplina = Disciplina.objects.get(
            id=disciplina_id
        )

        turma.semestre = request.POST.get(
            'semestre'
        )

        turma.vagas = request.POST.get(
            'vagas'
        )

        turma.save()

        return redirect('/turmas/')

    return render(
        request,
        'editar_turma.html',
        {
            'turma': turma,
            'disciplinas': disciplinas
        }
    )


def excluir_turma(request, turma_id):

    turma = Turma.objects.get(
        id=turma_id
    )

    turma.delete()

    return redirect('/turmas/')


# ==================================================
# MATRÍCULAS
# ==================================================

def listar_matriculas(request):

    if request.method == 'POST':

        aluno_id = request.POST.get(
            'aluno'
        )

        turma_id = request.POST.get(
            'turma'
        )

        aluno = Aluno.objects.get(
            id=aluno_id
        )

        turma = Turma.objects.get(
            id=turma_id
        )

        command = EfetuarMatriculaCommand(
            aluno,
            turma
        )

        command.execute()

        return redirect('/matriculas/')

    matriculas = Matricula.objects.all()

    alunos = Aluno.objects.all()

    turmas = Turma.objects.all()

    return render(
        request,
        'matriculas.html',
        {
            'matriculas': matriculas,
            'alunos': alunos,
            'turmas': turmas
        }
    )


def editar_matricula(
    request,
    matricula_id
):

    matricula = Matricula.objects.get(
        id=matricula_id
    )

    alunos = Aluno.objects.all()

    turmas = Turma.objects.all()

    if request.method == 'POST':

        aluno_id = request.POST.get(
            'aluno'
        )

        turma_id = request.POST.get(
            'turma'
        )

        matricula.aluno = Aluno.objects.get(
            id=aluno_id
        )

        matricula.turma = Turma.objects.get(
            id=turma_id
        )

        matricula.save()

        return redirect('/matriculas/')

    return render(
        request,
        'editar_matricula.html',
        {
            'matricula': matricula,
            'alunos': alunos,
            'turmas': turmas
        }
    )


def cancelar_matricula(
    request,
    matricula_id
):

    matricula = Matricula.objects.get(
        id=matricula_id
    )

    command = CancelarMatriculaCommand(
        matricula
    )

    command.execute()

    return redirect('/matriculas/')


def excluir_matricula(
    request,
    matricula_id
):

    matricula = Matricula.objects.get(
        id=matricula_id
    )

    matricula.delete()

    return redirect('/matriculas/')

