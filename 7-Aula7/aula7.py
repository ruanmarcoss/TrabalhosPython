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

dicionario_bandas = ['Nome' : '']
dicionario_bandas['Nome'] = 'Calipso'
dicionario_bandas['Nome'] = 'Dejavu'

print(dicionario_bandas)

dicionario = { 'Nome' : 'Ruan' , 'Sobrenome' : 'Silva'}
dicionario['Sobrenome'] = 'Marcos'
dicionario['CPF'] = '092.636.689-09'

for i in range(1,11):
    dicionario_pessoa = {'Nome' : '', 'Sobrenome' :'', 'CPF' : '', 'RG' : ''  }
    dicionario_pessoa['Nome'] = input('Digite o nome: ')
    dicionario_pessoa['SObrenome'] = input('Digite o Sobrenome: ')
    dicionario_pessoa['CPF'] = input('Digite o cpf: ')
    dicionario_pessoa['RG'] = input('Digite o rg: ')
    lista_pessoas.append(dicionario_pessoa)
