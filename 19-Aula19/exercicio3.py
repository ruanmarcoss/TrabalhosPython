# Aula 19 - 04-12-2019
# Lista com for e metodos

# Como comer um gigante.... é com um pedaço de cada vez.
# Na hora de fazer este exercicio, atentar para 

# Com o arquivo de cadastro.txt onde possui os seguintes dados: codigo cliente, nome, idade, sexo, e-mail e telefone
# 1 - Crie um metodo que gere e retorne uma lista com bibliotecas com os dados dos clientes
def ler():
    arquivo = open('19-Aula19/cadastro.txt','r')
    lista_dados = []
    for linha in arquivo:
        linha_1 = linha.strip().split(';')
        dicionario = {'Código':linha_1[0],'Nome':linha_1[1],'Idade': linha_1[2],'Sexo':linha_1[3],'E-mail':linha_1[4],'Telefone':linha_1[5]}
        lista_dados.append(dicionario)
    arquivo.close()
    return lista_dados
print(ler())
print('\n')
# 2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.
# Esta função tambem retornar uma lista com a biblioteca dos maiores de idades.
lista = ler()
maiores = open('19-Aula19/maiores.txt','a')
menores = open('19-Aula19/menores.txt','a')

for dicionario in lista:
    if int(dicionario['Idade'])>=18:
        maiores.write(f"{dicionario['Código']};{dicionario['Nome']};{dicionario['Idade']};{dicionario['Sexo']};{dicionario['E-mail']};{dicionario['Telefone']}\n")
    else:
        menores.write(f"{dicionario['Código']};{dicionario['Nome']};{dicionario['Idade']};{dicionario['Sexo']};{dicionario['E-mail']};{dicionario['Telefone']}\n")
maiores.close()
menores.close()
print('\n')

# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente.
def quantidade(lista):
    homens = open('19-Aula19/homens.txt', 'w')
    mulheres = open('19-Aula19/mulheres.txt', 'w')
    consulta_homens = 0
    consulta_mulheres = 0
    for consulta in lista:
        if dicionario['Sexo'] == 'm':
            homens.write(f"{dicionario['Código']};{dicionario['Nome']};{dicionario['Idade']};{dicionario['Sexo']};{dicionario['E-mail']};{dicionario['Telefone']}\n")
            consulta_homens += 1

        else:
            mulheres.write(f"{dicionario['Código']};{dicionario['Nome']};{dicionario['Idade']};{dicionario['Sexo']};{dicionario['E-mail']};{dicionario['Telefone']}\n")
            consulta_mulheres += 1
    homens.close()
    mulheres.close()
    return(f'A quantidade de homens é: {consulta_homens}, e a quantidade de mulheres é: {consulta_mulheres}')
print(quantidade(lista))

print('\n')



# 4 - Faça uma função de consulta de cadastro. A função deve receber o valor do código do cliente e deve imprimir na 
# tela os dados do cliente com f-string usando a lista do exercicio 1
#  4.1 - A pesquisa deve aparecer uma frase para as seguintes condições:
#           Mulheres até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!""
#           Mulheres acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor alegria! O seu 
#                                            cruch vai adorar!"
#           Mulheres acima de 18:  "Olá {nome}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico
#                                                com o dobro de sabor!!!"
#           Homens até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!""
#           Homens acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor Corriga de carros!  
#                                          A sua amada vai adorar!"
#           Homens acima de 18:  "Olá {nome}! Já experimentou nossa cerveja? alto teor alcoolico
#                                                com o dobro do amargor!!!"
#      Lembre-se: É importante que apareça a frase. Pois a mesma será encaminhada por e-mail pela equipe de marketing



