class Endereco:
    id = 0
    logradouro = ''
    numero = 0
    complemento = ''
    bairro = ''
    cidade = ''

    def exportar_txt(self, lista_endereco):
        #----- Cria um arquivo e atribui a uma variável 'arquivo'
        with open('33-Aula33/Aula33-4/endereco4.txt','a') as arquivo:
            #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
            for e in lista_endereco:
                arquivo.write(f"{str(e)}\n")
    
    def __str__(self):
        return f'{self.id};{self.logradouro};{self.numero};{self.complemento};{self.bairro};{self.cidade}'