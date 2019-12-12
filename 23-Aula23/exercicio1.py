# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)

class Cliente:
    def __init__(self,dadobruto):
        self.dado_bruto = dadobruto
        self.codigo_cliente = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None

    def tratar_dados(self):
        cliente = self.dado_bruto.strip().split(';')
        self.codigo_cliente = int(cliente [0])
        self.nome = (cliente [1])
        self.idade = int(cliente [2])
        self.sexo = (cliente [3])
        self.email = (cliente [4])
        self.telefone = (cliente [5])

c = Cliente(dadobruto)
c.tratar_dados()
print(f'Código: {c.codigo_cliente} \nNome: {c.nome} \nIdade: {c.idade} \nSexo: {c.sexo} \nE-mail: {c.email} \nTelefone: {c.telefone}')



    

