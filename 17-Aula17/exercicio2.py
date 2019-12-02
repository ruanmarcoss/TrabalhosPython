lista_banda = []
lista_album = []
lista_musica = []
menu = '''
##########################################
                BANDAS
##########################################

1 - Cadastro da Banda: 
2 - Cadastro do Álbum: 
3 - Cadastro da Música: 
4 - Sair: 

Escolha um opção: '''

while True:
    opcao = input(menu)
    if opcao == '1':
        lista_banda.append(input('Digite uma banda: '))
    elif opcao == '2':
        lista_album.append(input('Digite um álbum: '))
    elif opcao == '3':
        lista_musica.append(input('Digite uma música: '))
    elif opcao == '4':
        print(f'Cadastro de Banda: {lista_banda}\n Cadastro de Álbum: {lista_album}\n Cadastro de Música: {lista_musica}')
        break 
    else:
        print('Informação Inexistente!!! ')