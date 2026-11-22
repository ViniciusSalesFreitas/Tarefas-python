tarefas = ["estudar python", "ler"]

while True:
    print("\n1) Listar  2) Adicionar  3) Remover  4) Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        if len(tarefas) == 0:
            print("Nenhuma tarefa ainda.")
        else:
            for tarefa in tarefas:
                print("-", tarefa)
    elif opcao == "2":
        nova = input("Qual tarefa? ").strip().lower()
        if nova in tarefas:
            print("Essa tarefa já está na lista.")
        else:
            tarefas.append(nova)
            print("Adicionada!")
    elif opcao == "3":
        remover = input("Qual tarefa quer remover? ").strip().lower()
        if remover in tarefas:
            tarefas.remove(remover)
            print("Removida!")
        else:
            print("Essa tarefa não está na lista.")
    elif opcao == "4":
        print("Até mais!")
        break
    else:
        print("Opção inválida.")
