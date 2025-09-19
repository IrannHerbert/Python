print("  == Menu de cambio ==  ")
print("  1.Dólar\n  2.Euro\n  3.Libra\n  4.Lene\n  5.Sair")
moeda = float(input("Escolha uma moeda para conversão: "))

if moeda == 1:
    real_dolar = float(input("Digite um valor em reais para conversão: R$:"))
    conversao_dolar = real_dolar * 0.19
    print(f"Convertendo para Dólar você terá: {conversao_dolar:.5} Dólares")

if moeda == 2:
    real_euro = float(input("Digite um valor em reais para conversão: R$:"))
    conversao_euro = real_euro * 0.17
    print(f"Convertendo para Euro você terá: {conversao_euro:.5} Euros")

if moeda == 3:
    real_libra = float(input("Digite um valor em reais para conversão: R$:"))
    conversao_libra = real_libra * 0.15
    print (f"Convertendo para Libra você terá: {conversao_libra:.5} Libras")

if moeda == 4:
    real_leme = float(input("Digite um valor em reais para conversão: R$:"))
    conversao_leme = real_leme * 25
    print(f"Convertendo para Leme você terá: {conversao_leme:.5} Lemes")
    
elif moeda == 5:
    print("Obrigado por usar nosso conversor, até breve !")