
class PessoaModel:
    def __init__(self, nome, sobrenome, idade, id=0):#Quando o dado é opcional deve vir por último
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def __str__(self):
        return f'{self.id};{self.nome};{self.sobrenome};{self.idade}'