#aula 3 18-11-2019
#input e estruturas de decisão

lista = [1,2,3]
numero = 2

if 'Teti'.count('t') > 0:
    print('Existe "t" em "teti"')
if 'e' in 'teti':
    print('Existe "e" em "teti" ')

if 'M' in 'Teti':
    print('Não existe "M" em "Teti"')

if numero in lista:
    print('Existe')
else:
    print('Não existe')

nome = ''

if len(lista) == 0:
    print('Vazia')
else:
    print('não vazio')

if nome:
    print('preenchido')
else:
    print('vazio')

nome = ''
print(nome)
nome = 'ruan'
print(nome[2])

