# Lista de Tarefas (To-Do) no Terminal

Programa de lista de tarefas feito em Python com banco de dados SQLite, usado direto no terminal.

## Funcionalidades

- Adicionar tarefas com título e prioridade (baixa, média ou alta)
- Listar tarefas com status (pendente ou concluída) e data de criação
- Marcar tarefas como concluídas
- Editar título e prioridade
- Remover tarefas (com confirmação)
- Validação de entradas (ID inválido, título vazio, prioridade inválida)

## Tecnologias

- Python 3
- SQLite (módulo `sqlite3`, já incluso no Python)

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/Ribeiiro1109/todo-terminal.git
cd todo-terminal
```

2. Execute o programa:

```bash
python main.py
```

O banco de dados (`tarefas.db`) é criado automaticamente na primeira execução.

## Estrutura do projeto

```
todo-terminal/
├── banco.py   # acesso ao banco de dados (CRUD)
├── main.py    # menu e interação com o usuário
└── README.md
```

## O que pratiquei neste projeto

- CRUD completo com SQL (INSERT, SELECT, UPDATE, DELETE)
- Consultas parametrizadas para evitar SQL injection
- Separação de responsabilidades entre arquivos
- Validação de entrada do usuário
