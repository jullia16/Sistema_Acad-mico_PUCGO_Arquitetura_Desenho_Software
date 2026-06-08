from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    carga_horaria = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Turma(models.Model):
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE
    )
    semestre = models.CharField(max_length=10)
    vagas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.disciplina.nome} - {self.semestre}"


class Matricula(models.Model):
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE
    )

    data_matricula = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('aluno', 'turma')

    def __str__(self):
        return f"{self.aluno.nome} - {self.turma}"