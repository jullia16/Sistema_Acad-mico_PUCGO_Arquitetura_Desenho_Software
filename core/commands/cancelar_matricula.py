from .matricula_command import MatriculaCommand


class CancelarMatriculaCommand(MatriculaCommand):

    def __init__(self, matricula):
        self.matricula = matricula

    def execute(self):

        self.matricula.delete()