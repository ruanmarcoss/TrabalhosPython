# Aula 22 - 09/12/2019

# Crie uma classe cliente:

# 1) deve ter como atributos: codigo, cpf, nome, idade, sexo

# 2) como metodos: receber salario, comprar, pagar divida

# Quando recebe aumenta o dinheiro na carteira.

# quando compra aumenta os bens e diminui o dinheiro na carteira

# Se comprar e não tiver dinheiro o suficiente deve diminuir o dinheiro da carteira
# e aumentar a divida.

# Para pagar a divida tem que ter dinheiro o suficiente na carteira

# 3) atributos de estado: dinheiro na carteira, divida, bens

##### Atributos 
# codigo, cpf, nome, idade, sexo

##### Método 
# receber salario, comprar, pagar divida

#####


class Cliente:
    def __init__(self, codigo, cpf, nome, idade, sexo):
        self.codigo = codigo
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        #Atributos
        self.dinheiro_carteira = 0
        self.divida = 0
        self.bens = 0
        #Atriutos de estado

    def receber_salario(self,salario):
        if self.dinheiro_carteira == 0:
            self.dinheiro_carteira = salario
        else:
            self.dinheiro_carteira = self.dinheiro_carteira + salario

    

    def comprar(self,preco):
        if self.bens == 0:
            self.comprar = preco
        else:
            self.bens = self.comprar + preco

        
        
    # def pagar_divida(self,valor):
        

        

p = Cliente(20,'0926457070','Marcos',25,'Masculino')


print(f'O codigo é {p.codigo}')
print(f'O cpf é {p.cpf}')
print(f'O nome é {p.nome}')
print(f'A idade é {p.idade}')
print(f'O sexo é {p.sexo}')
print(f'Antes de receber o salário o total é: {p.dinheiro_carteira}')


p.dinheiro_carteira = 1500.85
p.receber_salario(500)
print(f'Depois de receber o salário o total é: {p.dinheiro_carteira}')

p.bens(500)
print(p.bens)
