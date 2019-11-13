# Aula 6 - 13-11-2019
# Listas


lista1 = []
lista2 = ['Marcela' ,  'Nicole' , 'Matheus' , 10]
lista3 = [1,2,3,5]

print(lista1)
print(lista2)
print(lista3)

lista1.append(lista2)
lista1.append(lista3)
#lista1.append( input ('digite sua idade'))
#lista_perguntas = [input ('artista = '), input('cantor = ')]

posicao = int(input ('digite a posicao: '))
print(lista2[posicao-1])
#print(lista_perguntas)
print(lista1)
#print(lista2)
#print(lista3)