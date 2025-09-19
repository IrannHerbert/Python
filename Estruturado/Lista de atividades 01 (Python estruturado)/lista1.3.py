#coleta de dados
arquivo = float(input("Digite o tamanho do arquivo em MB: "))
dowloand = float(input("Digite a sua velocidade de dowload em Mbps: "))

#conversão MB P/ Mb

arquivo_convertido = arquivo * 8 #para Mega bits

#conversão segundos p/ minutos
tempo = arquivo_convertido / dowloand #resultado em segundos
tempo_convertido = tempo / 60

print(f"Um arquivo de {arquivo} MB e uma conexão de {dowloand} Mbps,\nlevará {tempo_convertido:.2} minutos")