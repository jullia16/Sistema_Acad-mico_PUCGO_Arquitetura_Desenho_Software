# EduCore

Sistema Acadêmico desenvolvido em Django para gerenciamento de:

- Alunos
- Disciplinas
- Turmas
- Matrículas

## Tecnologias

- Python 3.13
- Django 6
- SQLite

## Padrão de Projeto

Command Pattern

Classes implementadas:

- EfetuarMatriculaCommand
- CancelarMatriculaCommand

## Funcionalidades

### Alunos
- Cadastrar
- Editar
- Excluir
- Listar

### Disciplinas
- Cadastrar
- Editar
- Excluir
- Listar

### Turmas
- Cadastrar
- Editar
- Excluir
- Listar

### Matrículas
- Efetuar matrícula
- Editar matrícula
- Cancelar matrícula
- Excluir matrícula
- Listar matrículas

## Como executar

Criar ambiente virtual:

```bash
python -m venv venv
```

Ativar ambiente virtual:

```bash
.\venv\Scripts\Activate.ps1
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar migrações:

```bash
python manage.py migrate
```

Iniciar servidor:

```bash
python manage.py runserver
```

Acessar:

http://127.0.0.1:8000