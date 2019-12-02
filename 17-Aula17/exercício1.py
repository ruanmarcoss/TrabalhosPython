menu = ''' 
###############################################################################
#                       I Festival de Cerveja em Ituroró                      #
###############################################################################

1 - Cadastro de Clientes
2 - Clientes Cadastrados
3 - Cadastro de Produtos
4 - Ver Produtos Cadastrados
5 - Vendas
6 - Relatório de Vendas
7 - Sair

Digite a opção desejada: '''
while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de Clientes')
    elif opcao == '2':
        print('Clientes Cadastrados')
    elif opcao == '3':
        print('Cadastro de Produtos')
    elif opcao == '4':
        print('Produtos Cadastrados')
    elif opcao == '5':
        print('Vendas')
    elif opcao == '6':
        print('Relatório de Vendas')
    elif opcao == '7':
        print('Sair')
        break #Usado para parar o looping
    else:
        print('Valor Inválido')