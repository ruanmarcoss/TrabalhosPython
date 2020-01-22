class Squad:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao = ''
        self.numero_pessoas = 0
        self.linguagem_BackEnd = ''
        self.framework_FrontEnd = ''

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numero_pessoas};{self.linguagem_BackEnd};{self.framework_FrontEnd}'

squad = Squad()        