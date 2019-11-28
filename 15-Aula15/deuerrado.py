



def cerveja(tipos):
    arquivo = open('tipo_cerveja.txt','w')
    arquivo.write('cerveja skol\n')
    arquivo.close

def ler():
    lista = []
    arquivo = open('tipos_cerveja.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_tipos = linha.split(';')
        # pessoa = {'tipo':lista_tipos[0], 'teor_alcoolico':lista_tipos[1], 'marca':lista_tipos[2]}
        lista.append(tipos)
    arquivo.close()
    return lista



# for p in ler():
# print(f"{p['tipo']} - {p['teor_alcoolico']} - {p['marca']}")


tipo = input('Digite o tipo: ')
teor_alcoolico = float(input('Digite o teor alcoolico: '))
marca = input('Digite a marca: ')

cerveja(tipos)