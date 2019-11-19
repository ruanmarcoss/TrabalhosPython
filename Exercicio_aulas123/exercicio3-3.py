#--- Exercicio 3  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um funcionário
#--- Funcionário: Nome Completo, CPF, Número do registro, Cargo e Salário
#--- Exiba os dados de salário liquido, descontando os tributos
#--- Deve ser calculado o valor do INSS -
#--- INSS -  de    0,00 ate 1751,81 - percetual =  8,0%
#---         de 1751,82 ate 2919,72 - percetual =  9,5%
#---         de 2919,72 ate 5839,45 - percetual = 11,0%
#--- Deve ser calculado o valor do IRRf - 
#--- IRRF -  de    0,00 ate 1903,98 - percetual =  0,0%
#---         de 1903,98 ate 2826,65 - percetual =  7,5%
#---         de 2826,66 ate 3751,05 - percetual = 15,0%
#---         de 3751,06 ate 4664,68 - percetual = 22,5%
#---         de 4664,69 ate ------- - percetual = 27,5%
#--- Base - http://www.calculador.com.br/calculo/salario-liquido 

def calculo_inss(salario):
    if(salario>0 and salario<=1751.81):
        inss = salario * 0.08
    elif(salario>1751.81 and salario<=2919.72):
        inss = salario * 0.090
    elif(salario>2919.72 and <=5839.45):
        inss = salario * 0.11
    else:
        inss = 642.34
    return inss


def calculo_irrf(salario):
    irrf = 0
    if(salario>1903.98 and salario <=2826.65):
        irrf = (((salario - inss) *0.075)-142.80)
    elif(salario>2826.66 and salario<=3751.05):
        irrf = (((salario - inss) *0.15)-)






print('='*50, '\n')

# nome = input('nome completo: ')
# cpf = input('cpf: ')
# num_registro = int(input('num_registro: '))
# cargo = input('cargo: ')
salario = float(input('salario: '))
