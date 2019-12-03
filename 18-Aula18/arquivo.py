def dados(codigo, nome, sexo, idade):
    inf = {'codigo': codigo, 'nome': nome, 'sexo': sexo, 'idade': idade}
    return inf

def salvar_dados(inf):
    arquivo = open('cadastro.txt','a')
    arquivo.write(f'{inf["codigo"]}; {inf["nome"]}; {inf["sexo"]}; {inf["idade"]}')
    arquivo.close

def ler_inf():
    arquivo = open('cadastro.txt','r')
    lista_dados = []
    for linha in arquivo:
        linha = linha.strip()
        dados_inf = linha.split(';')
        inf = dados(dados_inf[0], dados_inf[1], dados_inf[2], dados_inf[3])
        lista_dados.append(inf)
    arquivo.close()
    return lista_dados