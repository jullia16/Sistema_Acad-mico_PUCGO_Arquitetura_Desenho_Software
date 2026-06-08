from .matricula_command import MatriculaCommand
from core.models import Matricula


class EfetuarMatriculaCommand(MatriculaCommand):

    def __init__(self, aluno, turma):
        self.aluno = aluno
        self.turma = turma

    def execute(self):

        matricula = Matricula.objects.create(
            aluno=self.aluno,
            turma=self.turma
        )

        return matricula