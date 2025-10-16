#Qualculador de dias para estudar materia
 
dias = int(input("Digite os dias disponiveis para estudo da matéria: "))

materias = int(input("Digite quantas materias tem disponiveis: "))

calculador = dias / materias
print (f"Você tem {calculador:.0f} dias para cada matéria")