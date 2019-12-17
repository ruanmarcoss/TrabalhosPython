# Aula 21 - 16-12-2019
#Operadores in is ==

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como defult ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista = embaralhar(2,10)

a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

print(a)
print(b)
print(c)
print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.




lista = embaralhar(2,10,2)
print(lista)

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).

print(lista[0] is lista[1])
print(lista[0] == lista[1])

# 2) Qual é o maior valor destas duas listas 
print(f'O maior valor das listas é {max(max(lista))}')
print('\n')
# 3) Qual é o maior valor de cada lista
print(f'O maior valor da lista0 é {max(lista[0])} e o maior da lista1 é {max(lista[1])}')
print('\n')

# 4) Há o número 10 dentro da lista[0]?
if 10 in lista[0]:
    print('Tem')
else:
    print('Não tem')
print('\n')
# 5) Há o número 20 dentro da lista[1]?
if 20 in lista[1]:
    print('Tem')
else:
    print('Não tem')
print('\n')
# 6) Quantos números da lista[0] tem dentro da lista[1]?
numeros_iguais = 0
for igual1 in lista[0]:
    for igual2 in lista[1]:
        if igual1 == igual2:
            numeros_iguais+=1
            print(f'Tem {numeros_iguais} números iguais entre as listas')
        else:
            print(f'Não tem números iguais entre as listas')

# 7) Mostre os números da lista[0] que estão dentro da lista[1]
for i in lista[0]:
    if i in lista[1]:
        print(f'O número {i} está na lista1{lista[1]}')
    else:
        print('Não tem números iguais entre as listas')

# 8) Mutliplique a soma da lista[0] com cada item da lista[1]

soma = sum(lista[0])
for multiplica in lista[1]:
    print(soma * multiplica)

# 9) Faça uma divisão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!
def maior_numero():
    if max(lista[0]) > max(lista[1]):
        print(f'O maior número é da lista0: {max(lista[0])}')
        maior = (max(lista[0]))
    else:
        print(f'O maior número é da lista1: {max(lista[1])}')
        maior = (max(lista[1]))
    return maior

def menor_numero():
    if min(lista[0]) > min(lista[1]):
        print(f'O menor número é da lista0: {min(lista[0])}')
        menor = (min(lista[0]))
    else:
        print(f'O menor número é da lista1: {min(lista[1])}')
        menor = (min(lista[1]))
    return menor   
print('\n')
resultado = maior_numero()//menor_numero()
print(f'A divisão inteira entre o maior e o menor número da lista é: {resultado}')
if resultado in lista:
    print(f'O resultado: {resultado}, está dentro das listas')
else:
    print(f'O resultado: {resultado}, não está dentro das listas')

# 10) Verifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]
if max(lista[0]) in lista[1]:
    print(f'O maior número da lista[0]: {max(lista[0])}, está dentro da lista[1]')
else:
    print(f'O maior número da lista[0]: {max(lista[0])}, não está dentro da lista[1]')
print('\n')
if min(lista[1]) in lista[0]:
    print(f'O menor número da lista[1]: {min(lista[1])}, está dentro da lista[0]')
else:
    print(f'O menor número da lista[0]: {min(lista[1])}, não está dentro da lista[0]')
