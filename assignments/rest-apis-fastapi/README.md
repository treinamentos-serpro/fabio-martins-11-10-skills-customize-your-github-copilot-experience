# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para uma lista de tarefas usando o framework FastAPI. Você vai criar rotas para consultar, criar, atualizar e remover tarefas, validar os dados recebidos com Pydantic e devolver os códigos de status HTTP corretos.

**Habilidades praticadas:** rotas HTTP (GET, POST, PUT, DELETE), parâmetros de caminho e de consulta, modelos Pydantic, códigos de status e tratamento de erros

**Pré-requisitos:** Python básico, funções, listas e dicionários, e a noção de classes da atividade [Python Classes](../python-classes/).

**Como executar:**

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Depois, acesse `http://127.0.0.1:8000/docs` para testar sua API pela documentação interativa gerada automaticamente pelo FastAPI.

## 📝 Tarefas

### 🛠️ Primeira Rota

#### Descrição
Crie a aplicação FastAPI e uma rota que confirme que a API está no ar.

#### Requisitos
O programa completo deve:

- Criar a instância `app = FastAPI()`
- Definir uma rota `GET /` que retorne um JSON com uma mensagem de boas-vindas
- Definir uma rota `GET /health` que retorne `{"status": "ok"}`


### 🛠️ Listagem e Busca com Parâmetros

#### Descrição
Permita listar as tarefas e buscar uma tarefa específica pelo seu identificador.

#### Requisitos
O programa completo deve:

- Manter as tarefas em uma lista ou dicionário em memória, com pelo menos três tarefas de exemplo
- Definir `GET /tasks` que retorne todas as tarefas
- Aceitar o parâmetro de consulta opcional `done` (`true` ou `false`) para filtrar as tarefas por situação
- Definir `GET /tasks/{task_id}` que retorne uma tarefa pelo seu identificador


### 🛠️ Criação, Atualização e Remoção

#### Descrição
Implemente as operações de escrita usando modelos Pydantic para validar os dados enviados pelo cliente.

#### Requisitos
O programa completo deve:

- Criar um modelo Pydantic para a tarefa de entrada, com `title` (texto obrigatório) e `done` (booleano, com valor padrão `False`)
- Definir `POST /tasks` que adicione uma nova tarefa e retorne-a com o código de status `201 Created`
- Definir `PUT /tasks/{task_id}` que substitua os dados de uma tarefa existente
- Definir `DELETE /tasks/{task_id}` que remova uma tarefa e retorne o código `204 No Content`
- Gerar identificadores automáticos e únicos para as novas tarefas


### 🛠️ Erros, Validação e Documentação

#### Descrição
Torne sua API robusta: ela deve responder com erros claros quando algo der errado e manter a documentação automática coerente com o comportamento real.

#### Requisitos
O programa completo deve:

- Retornar `404 Not Found` com uma mensagem clara quando uma tarefa não existir (em `GET`, `PUT` e `DELETE`)
- Rejeitar com `422` (gerado pelo FastAPI) um `title` vazio ou com mais de 100 caracteres, usando `Field` do Pydantic
- Usar `response_model` em pelo menos uma rota para definir o formato da resposta
- Conferir na página `/docs` que todas as rotas aparecem com seus parâmetros e exemplos de corpo de requisição
