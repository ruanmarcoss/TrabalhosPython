# Aula 7 - 14-11-2019
# Dicionários

lista = []
dicionario = { 'Nome' : 'Ruan' , 'Sobrenome' : 'Silva'} 
print(dicionario)
print(dicionario[ 'Sobrenome'])

nome = 'Ruan'
lista_notas = [1,2,5,7]
media = sum(lista_notas)/ len(lista_notas)
situacao = 'reprovado'
if media >= 7:
    situacao = 'aprovado'
dicionario_alunos = {'Nome' : nome, 'Lista_Notas' : lista_notas, 'Media' : media, 'situacao' : situacao }

print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['situacao']} ")