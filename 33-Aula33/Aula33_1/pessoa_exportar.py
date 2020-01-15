def exportar_txt(lista_pessoa):
    #----- Cria um arquivo a atribui a uma variável 'arquivo'
    with open('33-Aula33/33-Aula33_1/pessoas.txt', 'a') as arquivo:
        for p in lista_pessoa:
            arquivo.write(f"{p['Id']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['Endereco_Id']}\n")