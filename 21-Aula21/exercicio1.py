# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.

#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.

# controle = 'n'
# while controle != 's':
#     n1 = float(input('digite um número: '))
#     n2 = float(input('digite outro número: '))
#     print(f'Soma de {n1} e {n2} é: {n1 + n2}')
#     print(f'Divisão de {n1} e {n2} é: {n1 / n2}')
#     print(f'Multiplicação de {n1} e {n2} é: {n1 * n2}')
#     print(f'Subtração de {n1} e {n2} é: {n1 - n2}')
#     controle = input('Digite "s" para sair: ')

# while True:          
#     try:
#         n1 = int(input('digite um número: '))
#         n2 = int(input('digite um número: '))
#         print(f'Soma de {n1} e {n2} é: {n1 + n2}')
#         print(f'Divisão de {n1} e {n2} é: {n1 / n2}')
#         print(f'Multiplicação de {n1} e {n2} é: {n1 * n2}')
#         print(f'Subtração de {n1} e {n2} é: {n1 - n2}')
#     except ValueError:
#         print('tá errado carai!')
#     else:
#         print('acerto mizeravi!')
#         pass
while True:          
    try:
        inteiro = int(input('digite um número: '))
        inteiro1 = int(input('digite um número: '))
        print(f'Divisão de {inteiro} e {inteiro1} é: {inteiro / inteiro1}')
    except (ValueError, ZeroDivisionError):
        print('tá errado carai,digite um número diferente de zero!(0)')
    else:
        print('acerto mizeravi!')
        break