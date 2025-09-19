"""""
Crie um programa em Python utilizando orientação a objetos
para gerenciar uma lista de produtos de um carrinho de
compras. Implemente uma classe chamada Produto, com
atributos privados (__nome, __preco e __quantidade) e
métodos públicos para acessar e modificar esses valores de
forma segura (getters e setters). Em seguida, implemente uma
classe CarrinhoDeCompras, que mantém uma lista de objetos
Produto e possui métodos para adicionar um produto ao
carrinho, remover um produto pelo nome, calcular o valor total
da compra e listar os produtos com suas quantidades e
preços individuais. O programa principal deve permitir que o
usuário adicione e remova produtos, visualize o conteúdo do
carrinho e o total da compra. Utilize encapsulamento para
proteger os dados dos produtos e boas práticas de
organização orientada a objetos.

"""""

class Produto:
#atributos privados da classe (Não acessiveis fora da classe)
    
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade


    def get_nome (self):
        return self.__nome
    
    def get_preco (self):
        return self.__preco
    
    def get_quantidade (self):
        return self.__quantidade
    
#O set tem por funcionalidade definir, ajustuar
    
    def set_nome (self, novo_nome):
        self.__nome = novo_nome

    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
    
    def set_quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade

#classe carrinho de compras, que vai guardar as manipulações dos produtos

class CarrinhoDecompras:
    
    def __init__(self):
        self.produtos = []

    def adicionar_produto (self, produto):
        self.produtos.append (produto)

    def remover_produto (self,nome):
        
        for produto in self.produtos:
            if produto.get_nome().lower() == nome.lower():
                self.produtos.remove(produto)
        print(f"Produto '{nome}' removido do carrinho.")

    def calcular_total (self):
        
        total = 0
        for produto in self.produtos:
            total += produto.get_preco() * produto.get_quantidade()
        return total
    
    def listar_produtos (self):
        if not self.produtos:
            print("Carrinho está vazio !")
        else:
            print("\n--- Produtos no carrinho ---")
            for produto in self.produtos:
                print(f"{produto.get_nome()} - R${produto.get_preco():.2f} x {produto.get_quantidade()}")
            print("----------------------------")
            print(f"Total: R$ {self.calcular_total():.2f}")

if __name__== "__main__":
    carrinho = CarrinhoDecompras ()
   
    while True:
        print("== Menu carrnho de compras virtual ==")
        print(" 1.Adicionar produto\n 2.Remover produto\n 3.Listar produtos\n 4.Ver o total da compra\n 5.Sair")
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o valor do produto: "))
            quantidade = int(input("Digite a quantidade do produto: "))
            produto = Produto (nome, preco, quantidade)
            carrinho.adicionar_produto (produto)
            print(f"Produto '{nome}' adicionado ao carrinho")

        elif escolha == 2:
            nome = input("Digite o nome do produto para remoção: ")
            carrinho.remover_produto (nome)
            print("O produto foi removido com sucesso !")

        elif escolha == 3:
            carrinho.listar_produtos()

        elif escolha == 4:
            print(f"O valor da soma total de produtos vai ser de {carrinho.calcular_total():.2f}")

        elif escolha == 5:
            print(" Saindo do programa.......\n.Obrigado por usar o carrinho virtual, até breve !")
            break

        else :
            print ("Escolha invalida, verifique e tente novamente.")
