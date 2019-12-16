# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int
from random import randint


lista1 = lista_simples_int(randint(5,100))
lista2 = lista_simples_int(randint(5,50))
lista3 = lista_simples_int(randint(5,75))


# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?

print((f'O tamanho da lista1 é {len(lista1)}'))
print('\n'*2)

# 1.2) Qual é o maior valor da lista2?

print((f'O maior valor da lista2 é {max(lista2)}'))
print('\n'*2)
# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?
print((f'O maior valor da lista2 é {max(lista2)}'))
print((f'O menor valor da lista2 é {min(lista2)}'))
print((f'A soma do maior e menor valor é {max(lista2) + min(lista2)}'))
print('\n'*2)

# 1.4) Qual é a média aritmética da lista1?
print(f'A média aritmética da lista1 é {sum(lista1) / len(lista1)} ')
print('\n'*2)

# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)
print(f'A soma da lista1 é {sum(lista1)}')
print(f'A soma da lista2 é {sum(lista2)}')
print(f'A soma da lista3 é {sum(lista3)}')
print(f'A soma da total das listas é {sum(lista1) + sum(lista2) + sum(lista3)}')
print('\n'*2)

# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.
for total in (lista1):
    print(f'Os valores da lista1 são {total}')
print('\n'*2)

# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError
lista_posicao = [5,9,10,25]
lista_listas = [lista1,lista2,lista3]
for posicao in lista_posicao:
    n = 0
    for indice in lista_listas:
        n += 1
        try:
            print(f'O número da lista{n} que está na posição {posicao} é: {indice[posicao]}')
        except IndexError:
            print(f'Erro de indexação na lista{n} posição {posicao}')

print('\n'*2)
# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).
def comparacao():
    if len(lista1) > len(lista2) and len(lista1) > len(lista3):
        print(f'A maior lista é a lista1 {len(lista1)}')
    elif len(lista2) > len(lista1) and len(lista2) > len(lista3):
        print(f'A maior lista é a lista2 {len(lista2)}')
    elif len(lista3) > len(lista1) and len(lista3) > len(lista1):
        print(f'A maior lista é a lista3 {len(lista3)}')
comparacao()
print('\n'*2)
# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.
maiores = max(lista1) + max(lista2) + max(lista3)
def menores():
    if min(lista1) < min(lista2) and min(lista1) < min(lista3):
        print(f'O menor valor é da lista1 {min(lista1)}')
        menor_numero = min(lista1)
    elif min(lista2) < min(lista1) and min(lista2) < min(lista3):
        print(f'O menor valor é da lista2 {min(lista2)}')
        menor_numero = min(lista2)
    elif min(lista3) < min(lista1) and min(lista3) < min(lista1):
        print(f'O menor valor é da lista3 {min(lista3)}')
        menor_numero = min(lista3)
    return menor_numero
resultado = maiores - menores()
print(f'A soma dos maiores números de todas as listas menos o menor valor de todas as listas é {resultado}')

print('\n'*2)
# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas
def numero_maior():
    if max(lista1) > max(lista2) and max(lista1) > max(lista3):
        print(f'O maior valor da lista1 é {max(lista1)}')
        maior = max(lista1)
    elif max(lista2) > max(lista1) and max(lista2) > max(lista3):
        print(f'O maior valor da lista2 é {max(lista2)}')
        maior = max(lista2)
    elif max(lista3) > max(lista1) and max(lista3) > max(lista1):
        print(f'O maior valor da lista3 é {max(lista3)}')
        maior = max(lista3)
    return maior
def numero_menor():
    if min(lista1) < min(lista2) and min(lista1) < min(lista3):
        print(f'O menor valor da lista1 é {min(lista1)}')
        menor = min(lista1)
    elif min(lista2) < min(lista1) and min(lista2) < min(lista3):
        print(f'O menor valor da lista2 é {min(lista2)}')
        menor = min(lista2)
    elif min(lista3) < min(lista1) and min(lista3) < min(lista1):
        print(f'O menor valor da lista3 é {min(lista3)}')
        menor = min(lista3)
    return menor
print(f'O resultado do maior valor de todas as listas mais o menor valor de todas as listas é {numero_maior() + numero_menor()}')