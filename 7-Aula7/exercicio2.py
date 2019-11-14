#--- Exercício 2 - Dicionários
#--- Escreva um programa que leia os dados de 11 jogadores
#--- Jogador: Nome, Posição, Número, Pernaboa
#--- Crie um dicionário para armazenar os dados
#--- Imprima todos os jogadores e seus dados



lista_jogadores = []

for i in range(1,12):
    jogador = {}
    jogador['Nome'] = input('Digite o nome: ')
    jogador['Posicao'] = input('Digite a posicao: ')
    jogador['Numero'] = int(input('Digite o numero: '))
    jogador['PernaBoa'] = input('Digite a PernaBoa: ')
    lista_jogadores.append(jogador)

print('\n*5') 

for i in lista_jogadores:
    print( i['Nome'], i['Posicao'], i['Numero'], i['PernaBoa'] )

