
lista_jogadores = []
lista_nomes = ['Nome' , 'Posicao' , 'Numero' , 'PernaBoa']


for j in range(1,3):
    jogador = {}
    for i in lista_nomes:
        jogador[i]=input(f'digite {i}: ')
    lista_jogadores.append(jogador)

print('\n'*2)
print(lista_jogadores)

for i in lista_jogadores:
    print(i['nome'])









