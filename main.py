import banco


def exibir_menu():
    print("\n===== LISTA DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Editar tarefa")
    print("5 - Remover tarefa")
    print("0 - Sair")


def pausar():
    input("\nPressione Enter para continuar...")


def adicionar():
    titulo = input("Título da tarefa: ").strip()
    if not titulo:
        print("O título não pode ficar vazio.")
        return
    prioridade = input("Prioridade (baixa/media/alta) [media]: ").strip().lower()
    if prioridade == "":
        prioridade = "media"
    if prioridade not in ("baixa", "media", "alta"):
        print("Prioridade inválida.")
        return
    banco.adicionar_tarefa(titulo, prioridade)
    print("Tarefa adicionada!")


def listar():
    tarefas = banco.listar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n--- Suas tarefas ---")
    for id_tarefa, titulo, prioridade, status, criada_em in tarefas:
        marca = "[x]" if status == "concluida" else "[ ]"
        print(f"{id_tarefa} {marca} ({prioridade}) {titulo} - {criada_em}")


def main():
    banco.criar_tabela()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar()
            pausar()
        elif opcao == "2":
            listar()
            pausar()
        elif opcao == "0":
            print("Até mais!")
            break
        else:
            print("Opção ainda não implementada.")


if __name__ == "__main__":
    main()
