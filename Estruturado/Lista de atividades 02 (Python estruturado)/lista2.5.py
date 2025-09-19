lista = []

while True:
    print(" == Menu interativo == ")
    print(" 1. Adicionar uma nova tarefa\n 2. Listar todas as tarefas\n 3. Remover uma tarefa pelo nome\n 4. Sair do programa")
    opcao = int(input("Selecione uma opção para prosseguir: "))
    
    if opcao == 1:
        tarefa = input(" Digite a nova tarefa: ")
        lista.append(tarefa)
    
    if opcao == 2:
        print(f"aqui está sua lista de tarefas atualizada\n{lista}")

    if opcao == 3:
        tarefa = input(" Digite qual tarefa deseja excluir: ")
        lista.remove (tarefa)

    if opcao == 4:
        print("Não se esqueça das suas tarfas, até breve !")
        break
    
    elif opcao != 1 and 4:
        print("Essa opção não está disponivel, escolha uma de 1 a 4 !")
        break
        
    
    #else:print("Não se esqueça das suas tarfas, até breve !")break