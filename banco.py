import sqlite3
from datetime import datetime


def conectar():
    return sqlite3.connect("tarefas.db")


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            prioridade TEXT NOT NULL DEFAULT 'media',
            status TEXT NOT NULL DEFAULT 'pendente',
            criada_em TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()


def adicionar_tarefa(titulo, prioridade="media"):
    conexao = conectar()
    cursor = conexao.cursor()
    criada_em = datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor.execute(
        "INSERT INTO tarefas (titulo, prioridade, criada_em) VALUES (?, ?, ?)",
        (titulo, prioridade, criada_em),
    )
    conexao.commit()
    conexao.close()


def listar_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, titulo, prioridade, status, criada_em FROM tarefas")
    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas


def concluir_tarefa(id_tarefa):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE tarefas SET status = 'concluida' WHERE id = ?", (id_tarefa,))
    conexao.commit()
    alterou = cursor.rowcount > 0
    conexao.close()
    return alterou


def remover_tarefa(id_tarefa):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conexao.commit()
    removeu = cursor.rowcount > 0
    conexao.close()
    return removeu


def editar_tarefa(id_tarefa, novo_titulo, nova_prioridade):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE tarefas SET titulo = ?, prioridade = ? WHERE id = ?",
        (novo_titulo, nova_prioridade, id_tarefa),
    )
    conexao.commit()
    editou = cursor.rowcount > 0
    conexao.close()
    return editou


if __name__ == "__main__":
    criar_tabela()
    print("Tabela criada com sucesso!")
