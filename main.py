tarefas = ["estudar python", "jogar", "ler"]

nova = input("Qual tarefa deseja adicionar? ")
if nova in tarefas:
    print("Essa tarefa já está adicionada.")
else:
    tarefas.append(nova)

resposta = input("Deseja remover alguma tarefa? (s/n) ")
if resposta == "s":
    remover = input("Qual tarefa quer remover? ")
    if remover in tarefas:
        tarefas.remove(remover)
    else:
        print("Essa tarefa não está na lista.")
elif resposta == "n":
    print("Ok, nenhuma tarefa removida.")
else:
    print("Digite apenas s ou n.")

print(tarefas)