# Aula 18 - 03-11-2019

# interação de lista com o for

# Usando o comando for vamos fazer uma interação de varialvel tipo coleção. A interação é (simplificadamente) 
# percorer toda a variavel e isolar seu valores.

# 1.1 Com a seguinte lista, use o for para interar esta tupla  e apresentar (usando o f-string) O nome da cerveja, 
# tipo da cerveja, o IBU da cerveja e o preço dela.

# cerveja = (('marca', 'tipo', 'ibu','preço'),
#            ('Skol','IPA','ultra-leve',3.50),
#            ('Brahma','lager','leve/media',3.45),
#            ('Kaiser','Americam Larger','leve',2.35),
#            ('Sol','larger mão','agua',1.19)
          


# 1.2 Crie uma função que receba esta tupla e devolva uma lista com um dicionários referenciando cada uma destas 
# cervejas.

cerveja = (('marca', 'tipo', 'ibu','preço'),
                ('Skol','IPA','ultra-leve',3.50),
              ('Brahma','lager','leve/media',3.45),
              ('Kaiser','Americam Larger','leve',2.35),
                ('Sol','larger mão','agua',1.19)
              )
cabecalho = cerveja[0]
dados = cerveja[1:]


for dados_cerveja in dados:
<<<<<<< HEAD
    for i in range(4):
      print(f'{cabecalho[i]} {dados_cerveja[i]}')

def receber(cerveja):
    cabecalho = cerveja[0] # Separa o cabeçalho da tupla
    dados = cerveja[1:] # Separa os dados da tupla
    lista_cerva = [] # Inicia uma lista para receber os dados
    for dados_cerveja in dados: # For para quebrar os dados, gerando o dicionário para armazenar os dados
        dicionario = {cabecalho[0]:dados_cerveja[0],cabecalho[1]:dados_cerveja[1],cabecalho[2]:dados_cerveja[2],cabecalho[3]:dados_cerveja[3]}
        lista_cerva.append(dicionario) # Adicionando o dicionário na lista
    return lista_cerva # Retorna a lista para o programa
print(receber(cerveja))
# [
# {'marca': 'Skol', 'tipo': 'IPA', 'ibu': 'ultra-leve', 'preço': 3.5}, 
# {'marca': 'Brahma', 'tipo': 'lager', 'ibu': 'leve/media', 'preço': 3.45},
# {'marca': 'Kaiser', 'tipo': 'Americam Larger', 'ibu': 'leve', 'preço': 2.35},
# {'marca': 'Sol', 'tipo': 'larger mão', 'ibu': 'agua', 'preço': 1.19}
# ]
=======
    print(f'{cabecalho[0]} {dados_cerveja[0]}')
    print(f'{cabecalho[1]} {dados_cerveja[1]}')
    print(f'{cabecalho[2]} {dados_cerveja[2]}')
    print(f'{cabecalho[3]} {dados_cerveja[3]}')


def dados_cerveja():
    lista = []
    for j in range():  
        dicionario = {}
        for i in cerveja:
            dicionario[i] = (f'{i}')
        lista.append(dicionario)
    return lista

dados_cerveja()

>>>>>>> 86996bcdae923b9d012769ee857f54a04af58d7e
