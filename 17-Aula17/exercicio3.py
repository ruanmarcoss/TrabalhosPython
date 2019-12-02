from random import randint
aleatorio = randint(1,10)
tentativas = 0
n = 0
# while not n == aleatorio:                               Outro modo de fazer, ensinado em sala de aula!!!
#     n = int(input('digite um número: '))
#     tentativas = tentativas +1
#     if n < aleatorio:
#         print('O número digitado é menor!')
#         continue
#     elif n > aleatorio:
#         print('O número digitado é maior!')
#         continue
#     elif n == aleatorio:
#         print(f'Acertou!! Você tentou {tentativas} vezes')
        
while True:
    n = int(input('digite um número: '))
    tentativas = tentativas +1
    if n < aleatorio:
        print('O número digitado é menor!')
        continue
    elif n > aleatorio:
        print('O número digitado é maior!')
        continue
    elif n == aleatorio:
        print(f'Acertou!! Você tentou {tentativas} vezes')
        break

    
    