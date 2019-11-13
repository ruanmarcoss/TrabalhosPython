# Aula 4 11-11-2019
# Estrutura de decisão



idade = 25
#----If simples, validação de apenas uma condição
if idade ==18:
    print('Maior')

#-----If com else
#-----Caso a condição validada pelo IF não seja verdadeira,
#-----O Else é executado
if (idade < 18):
   print('Menor')
else:
   print('Maior')


#----IF com Elif e else
#----Caso a condição validada if seja falsa
#----É validado a condição do Elif
#----Caso a condição do Elif seja falsa
#----Else é executado

if (idade < 18):
   print('Menor')
elif idade == 18:
    print('Silasco')
else:
   print('SilascoMaisAinda')


#----If com variável boolena
#----Em caso de variável booleana, não é necessário a validação(==True)
#----pois o If já valida se o conteúdo da variável é True, senão vai para o Else
ativo = True

if ativo:
    print('Logar')
else:
    print('Não pode')




