temp = int(input("Qual e a temperatura atual (Em °C) ?: "))

if temp < 0:
    print("Frio extremo")
elif temp > 0 and temp <= 10:
    print("Frio")
elif temp > 10 and temp <=25:
    print ("Ameno")
elif temp > 25 and temp <=35:
    print("Quente")
elif temp > 35 and temp <=45:
    print ("Muito quente")
else:
    print("sinto lhe informar, mas você está morando no sol !")