
base = int(input("Digite um número para base da potência: "))
expoente= int(input("Digite um número para o expoente da potência: "))


#potencia = base ** expoente
potencia2 = pow(base,expoente)
    
if expoente != 0 :
    print(f"O número {base} como base elevado a {expoente}° potência, terá como resultado {potencia2}")
    
elif expoente == 0:
    print(f"Todo número elevado a zero terá como resultado: {potencia2}")
