# Aula 19 - 04-12-2019
# Lista com for e metodos

cab = ['nome', 'telefone', 'email','idade']

pess   = [  ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
            ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
            ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
            ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]   
        ]


# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igua a 18 anos
#

def dados():
    nome = pess[0]
    telefone = pess[1]      #Atribuição dos daos em variáveis
    email = pess[2]
    idade = pess[3]
    lista = []
    for i in range(len(idade)): #Utilizando for in range e len, para fazer o for em todos os dados da lista 
        if int(pess[3][i]) >= 18: #Verificando se o valor é maior ou igual a 18, se for será atribuido ao dicionário.(Sendo convertida para int)
            dicionario = {'nome': nome[i], 'telefone': telefone[i], 'email': email[i], 'idade': idade[i]}
            lista.append(dicionario) # Incluindo o dicionário na lista vazia.
   
    return lista # Retornado a lista
print(dados()) # Chamando a função
print('\n'*2)

#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (não prescisa usar o f-string, .format())

for i in dados():
    print(i)
print('\n'*2)

# for lista_resultante in dados():
#     print('Nome: {}, Telefone: {}, Email: {}, Idade:{} '.format(nome, telefone, email, idade))

#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (usando o f-string)

for d in dados():
    print(f'Lista Resultante: {d}')































