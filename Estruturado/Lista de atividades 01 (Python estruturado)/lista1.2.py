a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))

#a, b = b, a  #desempacotamento (atribuição multipla)

temp = a   #Variavel temporaria
a = b
b = temp

print ("após a troca")
print(f"a = {a}")
print("b =",b)