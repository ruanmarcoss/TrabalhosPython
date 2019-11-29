#EXERCICIO - AULA 15
# arquivo = open('tiposdecerveja.txt','x')
# arquivo.write('cerveja\n')
# arquivo.close()





def cerveja(cerveja_dicionario):
    arquivo = open('tiposdecerveja.txt','w')
    arquivo.write(f"{cerveja_dicionario['nome']};{cerveja_dicionario['tipo']};{cerveja_dicionario['teor alcoolico']}\n")
    arquivo.close

def ler():
    lista = []
    arquivo = open('tiposdecerveja.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja_inf = {'nome':lista_linha[0], 'tipo':lista_linha[1], 'teor alcoolico':lista_linha[2]}
        lista.append(cerveja_inf)
    arquivo.close()
    return lista


nome =  input('nome: ')
tipo = input('tipo: ')
teor_alocoolico = float(input('teor alcoolico: '))


for c in ler():
    print(f"{c['nome']} -  {c['tipo']} - {c['teor_alocoolico']}")
    






# def receber():
#     nome =  input('nome: ')
#     tipo = input('tipo: ')
#     teor_alocoolico = float(input('nome: '))
#     cerveja_inf = {'nome':nome, 'tipo':tipo, 'teor alocoolico':teor_alocoolico}
#     return cerveja_inf

# def cadastro(receber):