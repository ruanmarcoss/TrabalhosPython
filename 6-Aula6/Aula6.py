# Aula 6 - 13-11-2019
# Listas

#incialização de uma variável do tipo lista vazia
lista1 = []
#incialização de uma variável lista, com elementos
lista2 = ['Marcela' ,  'Nicole' , 'Matheus' , 10]
#lista de inteiros
lista3 = [1,2,3,5]
#lista de tipos diferentes
lista4 = [1, "Ruan", 12.5]


#-----Impressão das listas criadas
print(lista1)
print(lista2)
print(lista3)
print(lista4)

#----Adicionando elementos em uma lista já criada
lista1.append(lista2)
lista1.append(lista3)

#-----Impressão das listas modificadas
print(lista1)
print(lista2)
print(lista3)


#-----Criação de lista com dados vindos da função Input
lista_perguntas = [input ('artista = '), input('cantor = ')]
print(lista_perguntas)



#-----Recuperando um dado de uma posição específica da lista
posicao = int(input ('digite a posicao: '))
print(lista2[posicao-1])