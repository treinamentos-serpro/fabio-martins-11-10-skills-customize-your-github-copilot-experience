
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construa o clássico jogo de adivinhar palavras usando strings, loops e entrada de dados do usuário em Python. Você criará um jogo da Forca em que o jogador adivinha letras para revelar uma palavra oculta antes de esgotar as tentativas.

**Habilidades praticadas:** Manipulação de strings, loops, condicionais, seleção aleatória

## 📝 Tarefas

### 🛠️ Seleção Aleatória de Palavras

#### Descrição
Crie a lógica que escolhe, a cada partida, uma palavra aleatória de uma lista predefinida.

#### Requisitos
O programa completo deve:

- Definir uma lista predefinida de palavras
- Selecionar uma palavra aleatoriamente ao iniciar cada partida


### 🛠️ Palpites e Progresso

#### Descrição
Aceite palpites de letras do jogador e mostre o progresso atual da palavra oculta.

#### Requisitos
O programa completo deve:

- Aceitar palpites de letras usando `input()`
- Mostrar o progresso atual no formato `_ _ _`, revelando as letras já acertadas


### 🛠️ Tentativas e Fim de Jogo

#### Descrição
Controle as tentativas restantes e defina quando a partida termina, informando o resultado ao jogador.

#### Requisitos
O programa completo deve:

- Rastrear o número de tentativas incorretas restantes
- Encerrar quando a palavra for adivinhada ou as tentativas se esgotarem
- Exibir mensagens de vitória ou derrota