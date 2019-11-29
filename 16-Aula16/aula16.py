# Aula 16 29-11-2019
# ????????
#cadastro de playlist
#lendo musica, artista e album



from faixa import criar_faixa,salvar_faixa,ler_faixa


musica = input('digite a música: ')
album = input('digite o album: ')
artista = input('digite o artista: ')

faixa = criar_faixa(musica,album,artista)
salvar_faixa(faixa)
lista = ler_faixa()

for faixa in lista:
    print(f'{faixa["musica"]} - {faixa["album"]} - {faixa["artista"]}' )
