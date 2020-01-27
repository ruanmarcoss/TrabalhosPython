from Model.model_backend import BackEnd
from Model.model_frontend import FrontEnd
from Model.model_sgbds import Sgbds
class Squad:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao = ''
        self.numero_pessoas = 0
        self.fk_linguagem_backend = BackEnd()
        self.fk_framework_frontend = FrontEnd()
        self.fk_sgbds = Sgbds()

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numero_pessoas};{self.fk_linguagem_backend};{self.fk_framework_frontend};{self.fk_sgbds}'

squad = Squad()    