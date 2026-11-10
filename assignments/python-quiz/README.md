# 📘 Atividade: Quiz de Programação

## 🎯 Objetivo

Construa um quiz de perguntas e respostas no terminal. Você vai guardar as perguntas em listas e dicionários, percorrê-las com loops, calcular a pontuação e tratar entradas inválidas com `try`/`except`.

**Habilidades praticadas:** listas, dicionários, loops, condicionais, tratamento de erros com `try`/`except`

## 📝 Tarefas

### 🛠️ Perguntas em Listas e Dicionários

#### Descrição

Crie a estrutura de dados que guarda as perguntas do quiz. Cada pergunta deve ter um enunciado, uma lista de opções e a resposta correta.

#### Requisitos

O programa completo deve:

- Guardar pelo menos três perguntas em uma lista
- Representar cada pergunta como um dicionário com as chaves `"question"`, `"options"` e `"answer"`
- Exibir a primeira pergunta com suas opções numeradas a partir de 1

### 🛠️ Loop do Quiz e Pontuação

#### Descrição

Percorra todas as perguntas, pergunte a resposta do jogador e conte os acertos.

#### Requisitos

O programa completo deve:

- Percorrer todas as perguntas com um loop `for`
- Ler a resposta do jogador com `input()`
- Somar um ponto para cada resposta correta
- Exibir a pontuação final no formato `Você acertou X de Y perguntas`

### 🛠️ Entradas Inválidas

#### Descrição

Impeça que o programa quebre quando o jogador digitar algo que não é um número ou um número fora das opções.

#### Requisitos

O programa completo deve:

- Converter a resposta com `int()` dentro de um bloco `try`
- Capturar `ValueError` com `except` e pedir a resposta novamente
- Rejeitar números fora da faixa de opções disponíveis e pedir novamente
