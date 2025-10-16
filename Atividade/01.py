#Criaçao da classe que vai ser responsavel pelas tarefas
class Atividade:
    def __init__(self,descricao):
        self.descricao = descricao
        self.concluida = False

    def marcar_concluida(Self):
        self.concluida = True

    def __str__(self):
        status = "Concluida !"
        return f"{status}{self.descricao}"