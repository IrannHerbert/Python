saldo = 1000.00

while True:
    print(" == Menu IFB bank ==\n 1. Depositar\n 2. Sacar\n 3. Saldo\n 4. Sair")
    escolha = int(input("Digite a opção desejada (1 a 4): "))
    
    if escolha == 1:
        deposito= float(input("Digite um valor para ser depositado R$:"))
        saldo = saldo + deposito
        print(f"O saldo atualizado será R${saldo}")
    
    if escolha == 2:
        saque = float (input("Digite um valor para saque: R$"))
        saldo = saldo - saque
        print(f"O saldo atualizado R${saldo}")
        
    if escolha == 3:
        print (f"O saldo atualizado é R${saldo}")

    if escolha == 4:
        print ("Obrigado por usar nosso banco, até breve !")
        break