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

    #     print(f'Aumenta o dinheiro na carteira em R${salario}')

    # def comprar(self,preco):
    #     self.dinheiro_carteira -= preco
    #     print(f'Dinheiro da carteira diminui em R${preco}')
    #     self.bens += preco
    #     print(f'Os seus bens aumentam em R${preco}')
        
        
    # def pagar_divida(self,valor):
        

        

p = Cliente(20,'0926457070','Marcos',25,'Masculino')
p2 = Cliente(20,'0926457070','Pedro',25,'Masculino')

print(f'O codigo é {p.codigo}')
print(f'O cpf é {p.cpf}')
print(f'O nome é {p.nome}')
print(f'A idade é {p.idade}')
print(f'O sexo é {p.sexo}')
print(f'{p.dinheiro_carteira}')

p.dinheiro_carteira = 1500.85
p.receber_salario(500)
print(p.dinheiro_carteira)