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


def ler_id():
    texto = input("ID da tarefa: ").strip()
    if not texto.isdigit():
        print("ID inválido. Digite apenas números.")
        return None
    return int(texto)


def ler_prioridade():
    prioridade = input("Prioridade (baixa/media/alta) [media]: ").strip().lower()
    if prioridade == "":
        return "media"
    if prioridade not in ("baixa", "media", "alta"):
        print("Prioridade inválida.")
        return None
    return prioridade


def adicionar():
    titulo = input("Título da tarefa: ").strip()
    if not titulo:
        print("O título não pode ficar vazio.")
        return
    prioridade = ler_prioridade()
    if prioridade is None:
        return
    banco.adicionar_tarefa(titulo, prioridade)
    print("Tarefa adicionada!")


def listar():
    tarefas = banco.listar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return False
    print("\n--- Suas tarefas ---")
    for id_tarefa, titulo, prioridade, status, criada_em in tarefas:
        marca = "[x]" if status == "concluida" else "[ ]"
        print(f"{id_tarefa} {marca} ({prioridade}) {titulo} - {criada_em}")
    return True


def concluir():
    if not listar():
        return
    id_tarefa = ler_id()
    if id_tarefa is None:
        return
    if banco.concluir_tarefa(id_tarefa):
        print("Tarefa concluída!")
    else:
        print("Tarefa não encontrada.")


def editar():
    if not listar():
        return
    id_tarefa = ler_id()
    if id_tarefa is None:
        return
    novo_titulo = input("Novo título: ").strip()
    if not novo_titulo:
        print("O título não pode ficar vazio.")
        return
    nova_prioridade = ler_prioridade()
    if nova_prioridade is None:
        return
    if banco.editar_tarefa(id_tarefa, novo_titulo, nova_prioridade):
        print("Tarefa editada!")
    else:
        print("Tarefa não encontrada.")


def remover():
    if not listar():
        return
    id_tarefa = ler_id()
    if id_tarefa is None:
        return
    confirmacao = input("Tem certeza que deseja remover? (s/n): ").strip().lower()
    if confirmacao != "s":
        print("Remoção cancelada.")
        return
    if banco.remover_tarefa(id_tarefa):
        print("Tarefa removida!")
    else:
        print("Tarefa não encontrada.")


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
        elif opcao == "3":
            concluir()
            pausar()
        elif opcao == "4":
            editar()
            pausar()
        elif opcao == "5":
            remover()
            pausar()
        elif opcao == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
