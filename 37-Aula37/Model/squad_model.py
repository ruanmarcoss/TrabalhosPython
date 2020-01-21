class Squad:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao = ''
        self.numero_pessoas = 0
        self.linguagem_backend = ''
        self.framework_frontend = ''

    def __str__(self):
        return f'{self.nome};{self.descricao};{self.numero_pessoas};{self.linguagem_backend};{self.framework_frontend}'