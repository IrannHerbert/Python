print ("== Provas ==")
p1 = float(input("Digite a nota da prova 01: "))
p2 = float(input("Digite a nota da prova 02: "))
mp = (p1 + p2) / 2

print ("== Teste ==")
t1 = float(input("Digite a nota do teste 01: "))
t2 = float(input("Digite a nota do teste 02: "))
mt = (t1 + t2) / 2

mf = (mp * 0.80) + (mt * 0.20)

if mf >= 6.0:
    print(f"Com a média final das provas {mf:.2} \n== O aluno está APROVADO ! ==")
elif mf < 6.0:
    print(f"Com a média final das provas {mf:.2}\n== O aluno está REPROVADO ! ==")