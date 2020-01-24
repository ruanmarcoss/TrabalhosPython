class Squad:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao = ''
        self.numero_pessoas = 0
        self.fk_linguagem_backend = ''
        self.fk_framework_frontend = ''
        self.fk_sgbds = ''

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numero_pessoas};{self.fk_linguagem_backend};{self.fk_framework_frontend};{self.fk_sgbds}'

squad = Squad()        