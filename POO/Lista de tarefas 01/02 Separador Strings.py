"""""
Faça um programa em Python orientado a objetos que, a
partir de uma string digitada pelo usuário, imprima:
◦ O número de caracteres da string;
◦ A string com todas suas letras em maiúsculo;
◦ A string com todas suas letras em minúsculo;
◦ O número de vogais da string;
◦ Se a substring “IFB” aparece no texto (ignorando
maiúsculas/minúsculas).

Refazer

"""""
class String:
    
    def __init__(self, texto):
        self.texto = texto

    def contar_caracteres(self):
        return len(self.texto)

    def em_maiusculas(self):
        return self.texto.upper()

    def em_minusculas(self):
        return self.texto.lower()

    def contar_vogais(self):
        vogais = 'aeiouAEIOU'
        return sum(1 for c in self.texto if c in vogais)

    def contem_ifb(self):
        return 'ifb' in self.texto.lower()

    def exibir_resultados(self):
        print("Número de caracteres:", self.contar_caracteres())
        print("Texto em maiúsculas:", self.em_maiusculas())
        print("Texto em minúsculas:", self.em_minusculas())
        print("Número de vogais:", self.contar_vogais())
        print("Contém 'IFB'?:", "Sim" if self.contem_ifb() else "Não")



def main():
    entrada = input("Digite um texto: ")
    analise = String(entrada)
    analise.exibir_resultados()


if __name__ == "__main__":
    main()
    