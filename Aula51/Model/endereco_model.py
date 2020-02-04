
class EnderecoModel:
    def __init__(self, rua, complemento, numero, cep, id=0):
        self.id = id
        self.rua = rua
        self.complemento = complemento
        self.numero = numero
        self.cep = cep

    # def __str__(self):
    #     return f"{self.id};{self.rua};{self.complemento};{self.numero};{self.cep}"