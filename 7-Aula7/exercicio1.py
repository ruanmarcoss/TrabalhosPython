#--- Exercício 1
#--- Escreva programa que leia os dados de cerveja
#--- Cerveja: Marca, Tipo, IBU, ABV, EBC, Volume
#--- Crie um dicionário para armazenar os dados
#--- Imprima os dados do dicionário (não dicionário completo)


marca = input('Digite a marca:')
tipo = input('Digite o tipo:')
ibu = float(input('Digite o IBU:'))
abv = input('Digite o ABV:')
ebc = input('Digite o EBC:')
volume = float(input('Digite o Volume:'))




inf_cerveja = {'marca' : marca, 'tipo' : tipo, 'ibu' : ibu, 'abv' : abv, 'ebc' : ebc, 'volume' : volume}
print(f"{inf_cerveja['marca']} - {inf_cerveja['tipo']} - {inf_cerveja['ibu']} - {inf_cerveja['abv']} - {inf_cerveja['ebc']} - {inf_cerveja['volume']}")


