# Crie um programa que leia 4 notas
# Imprima a maior nota
# Imprima a menor nota
# Imprima a média
# Imprima se o aluno foi aprovado ou reprovado (Média 7.0)

print ('='*50, '\n'*5)


nota1 = int(input ('Digite a nota1 ='))
nota2 = int(input ('Digite a nota2 ='))
nota3 = int(input ('Digte a nota3 ='))
nota4 = int(input ('Digite a nota4 ='))

if nota1 > nota2 and nota1 > nota3 and nota1 > nota4:  
    print(f'nota1 {nota1} é a maior')
if nota2 > nota1 and nota2 > nota3 and nota2 > nota4:
    print(f'nota2 {nota2} é a maior')
if nota3 > nota1 and nota3 > nota2 and nota3 > nota4:
    print(f'nota3 {nota3} é a maior')
if nota4 > nota1 and nota4 > nota2 and nota4 > nota3:
    print(f'nota4 {nota4} é a maior')



if nota1 < nota2 and nota1 < nota3 and nota1 < nota4:  
    print(f'nota1 {nota1} é a menor')
if nota2 < nota1 and nota2 < nota3 and nota2 < nota4:
    print(f'nota2 {nota2} é a menor')
if nota3 < nota1 and nota3 < nota2 and nota3 < nota4:
    print(f'nota3 {nota3} é a menor')
if nota4 < nota1 and nota4 < nota2 and nota4 < nota3:
    print(f'nota4 {nota4} é a menor')


media = (nota1 + nota2 + nota3 + nota4) / 4


print(f'média das notas: {media}')


if media >= 7:
    print(f'Aluno aprovado = {media}')




print ('='*50, '\n'*5)