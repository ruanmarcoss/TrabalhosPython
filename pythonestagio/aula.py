#Aula 4
# Fazer um programa que leia 2 números
# Realize as 4 operações matemáticas
# Imprima o resultado das operações 
# Diga qual número é o maior dos dois números

numero1 = int(input ('Digite numero1 ='))
print(numero1)
numero2 = int(input ('Digite numero2 ='))
print(numero2)


resultado1 = numero1 + numero2
resultado2 = numero1 - numero2
resultado3 = numero1 / numero2
resultado4 = numero1 * numero2

print(f'soma : {numero1} + {numero2} = {resultado1}')
print(f'sub : {numero1} - {numero2} = {resultado2}')
print(f'div : {numero1} / {numero2} = {resultado3}')
print(f'mult : {numero1} * {numero2} = {resultado4}')

if numero1 > numero2:
    print(f'numero1 {numero1} é o maior')
if numero2 > numero1:
    print(f'numero2 {numero2} é o maior')
else:
    print(f'os numeros {numero1} e {numero2} são iguais')



