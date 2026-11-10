from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Lista de Tarefas")


class TaskIn(BaseModel):
    title: str
    done: bool = False


tasks = {
    1: {"id": 1, "title": "Estudar Python", "done": True},
    2: {"id": 2, "title": "Praticar FastAPI", "done": False},
    3: {"id": 3, "title": "Escrever testes", "done": False},
}
next_id = 4


# Tarefa 1: crie as rotas GET / e GET /health aqui.


# Tarefa 2: crie as rotas GET /tasks e GET /tasks/{task_id} aqui.


# Tarefa 3: crie as rotas POST, PUT e DELETE aqui.


# Tarefa 4: adicione tratamento de erros 404 e validação do título aqui.
