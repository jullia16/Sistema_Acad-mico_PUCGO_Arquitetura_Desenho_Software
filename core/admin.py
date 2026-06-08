from django.contrib import admin
from .models import Aluno, Disciplina, Turma, Matricula

admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Matricula)