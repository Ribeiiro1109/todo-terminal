import banco


def exibir_menu():
    print("\n===== LISTA DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Editar tarefa")
    print("5 - Remover tarefa")
    print("0 - Sair")


def main():
    banco.criar_tabela()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "0":
            print("Até mais!")
            break
        else:
            print("Opção ainda não implementada.")


if __name__ == "__main__":
    main()
