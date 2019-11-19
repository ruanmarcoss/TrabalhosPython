# Aula 9 -19-11-2019
#---Crie um programa que:
#--- 1-Leia dois números inteiros
#--- 2-Calcule a soma entre dois números através de um método
#--- 3-Calcule a subtração entre dois números através de um método
#--- 4-Calcule a multiplicação entre dois números através de um método
#--- 5-Calcule a divisão inteira entre dois números através de um método
#--- 6-Calcule a divisão fracionada entre dois números através de um método
#--- 7-Calcule resto da divisão entre dois números através de um método
#--- 8-Calcule a raiz entre os dois números através de um método
#--- 9-Separa os métodos em outro arquivo

from calculo_metodo import soma, subtracao, multiplicacao,  divisao_int, divisao_frac, resto, raiz

n1 = int(input('digite n1: '))
n2 = int(input('digite n2: '))


print(f'A soma entre {n1} e {n2} é: {soma(n1,n2)}')
print(f'A subtração entre {n1} e {n2} é: {subtracao(n1,n2)}')
print(f'A multiplicação entre {n1} e {n2} é: {multiplicacao(n1,n2)}')
print(f'A divisão inteira entre {n1} e {n2} é: {divisao_int(n1,n2)}')
print(f'A divisão fracionada entre {n1} e {n2} é: {divisao_frac(n1,n2)}')
print(f'O resto entre {n1} e {n2} é: {resto(n1,n2)}')
print(f'A raiz entre {n1} e {n2} é: {raiz(n1,n2)}')



