#EXERCICIO - AULA 15

def cerveja(cerveja_dicionario):
    arquivo = open('tipos de cerveja.txt','a')
    arquivo.write(f"{cerveja_dicionario['nome']};{cerveja_dicionario['tipo']};{cerveja_dicionario['teor alcoolico']}\n")
    arquivo.close

def ler():
    lista = []
    arquivo = open('tipos de cerveja.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja_inf = {'nome':lista_linha[0], 'tipo':lista_linha[1], 'teor alcoolico':lista_linha[2]}
        lista.append(pessoa)
    arquivo.close()
    return lista

def receber():
    nome =  input('nome: ')
    tipo = input('tipo: ')
    teor_alocoolico = float(input('nome: '))
    cerveja_inf = {'nome':nome, 'tipo':tipo, 'teor alocoolico':teor_alocoolico}
    return cerveja_inf

def cadastro(receber):
    for c in receber():
        print(f"{c['nome']} -  {c['tipo']} - {c['teor_alocoolico']}")
    
    
