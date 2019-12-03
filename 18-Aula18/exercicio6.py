# Aula 18 - 03-11-2019

# Festa da HBSIS

# 1 - Faça uma função que leia do arquivo cadastro.txt e retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição: codigo, nome, sexo, idade

# 2 - Como a entrada da festa é mais barata para mulheres (R$ 15,00) do que para os homens (R$ 35,00) 
# deve-se separar os dois em duas listas separadas e salvar em arquivos separados. Como é uma festa de arromba,
# menores de idade não podem entrar.

# 3 - Faça uma terceira função que ao digitar o código do participante ele imprima o nome do participante, 
# o valor do ingresso, e em caso de menores de idade apareça o texto "Entrada Proibida!"


# arquivo = open('cadastro.txt','a')
# arquivo.write('codigo')

from arquivo import dados,salvar_dados,ler_inf

codigo = int(input('digite o codigo: '))
nome = input('digite o nome: ')
sexo = input('digite o sexo: ')
idade = int(input('digite a idade: '))

inf = dados(codigo,nome,sexo,idade)
salvar_dados(inf)
lista = ler_inf()

for inf in lista:
    print(f'{inf["codigo"]} - {inf["nome"]} - {inf["sexo"]} - {inf["idade"]}')


