#Criaçao da classe que vai ser responsavel pelas tarefas
class Atividade:
    def __init__(self,descricao):
        self.descricao = descricao
        self.concluida = False

    def marcar_concluida(Self):
        self.concluida = True

    def __str__(self):
        status = "Concluida !" if self.concluida else "Não concluida !"
        return f"{status}{self.descricao}"
    
    class BancoDeDadosTarefas:
        _instancia = nome

        def __new__(cls):

