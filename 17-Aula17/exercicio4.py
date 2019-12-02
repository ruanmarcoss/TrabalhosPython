def cadastro_cliente(numero_funcao):
    lista_dados = ['codigo_cliente', 'CPF', 'nome_completo', 'data_nascimento',
    'estado', 'cidade', 'cep', 'bairro', 'rua', 'numero_casa', 'complemento']

    lista = []
    for j in range(numero_funcao):
        dicionario = {}
        for i in lista_dados:
            dicionario[i]= input(f'{i}: ')
        lista.append(dicionario)
    return lista
numero = int(input('Digite o número de Cadastros: '))
lista_cadastro = cadastro_cliente(numero)

# Criar uma função para salvar em arquivo: 

for cliente in lista_cadastro:
        cliente_chave = list(cliente.keys())
    for chaves in cliente_chave:
        




arquivo.write()



arquivo.close()