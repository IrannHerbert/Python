producao = float(input("Digite o preço de produção do veiculo: "))

distribuidor = 12 / producao * 100 
impostos = 30 / producao * 100
custo = producao + distribuidor + impostos

print(f"O preço final do carro será de: R${custo:.6}! \nSendo: \n12% do distribuidor R${distribuidor:.6} \n30% em impostos: R${impostos:.6}")