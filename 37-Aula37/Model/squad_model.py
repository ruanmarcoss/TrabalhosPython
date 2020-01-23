class Squad:
    def __init__(self):
        self.Id = 0
        self.Nome = ''
        self.Descricao = ''
        self.NumeroPessoas = 0
        self.LinguagemBackEnd = ''
        self.FrameWorkFrontEnd = ''

    def __str__(self):
        return f'{self.Id};{self.Nome};{self.Descricao};{self.NumeroPessoas};{self.LinguagemBackEnd};{self.FrameWorkFrontEnd}'

squad = Squad()        