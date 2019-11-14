# Aula 4_2 13-11-2019
# Booleanas


#----Variável booleana simples com True ou False
validador = false
#----Substituição do valor inicial
validador = true


#----Criação de variável booleana através de expressão de igualdade
idade = 18
validador = ( idade == 18 )
print(validador)
#----Criação de variável booleana através de expressão da diferença
validador = ( idade != 18 )
print(validador)
#----Criação de variável booleana através de expressão de maior
validador = ( idade > 18 )
print(validador)
#----Criação de variável booleana através de expressão da menor
validador = ( idade < 18 )
print(validador)
#----Criação de variável booleana através de expressão de maior e igual
validador = ( idade >= 18 )
print(validador)
#----Criação de variável booleana através de expressão de menor e igual
validador = ( idade <= 18 )
print(validador)

#----Criação de variável booleana através de negação
validador = not True
validador = not False

sorteado = 'Marcela'
validador = (sorteado== 'Mateus' and sorteado=='Marcela')
validador = (sorteado== 'Mateus' or sorteado=='Marcela')