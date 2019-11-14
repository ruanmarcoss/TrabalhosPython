#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)



print ('='*50, '\n'*10)

nomes = []
notas = []
media = 0
a = 0
b = 1
c = 2
d = 3

for i in range(0,10):
    nomes.append(input(f'Digite o nome do aluno {i+1}: '))
    for j in range(0,4):
        notas.append(float(input(f'Digite a nota {j+1}: ')))

for alunos in nomes:
     media = (notas[a]+notas[b]+notas[c]+notas[d])/4
     print(f'\nNome: {alunos}')
     print(f'Média: {media}')
     if media >= 7:
          print('Aprovado!')
     else:
          print('Reprovado!')
     a = a+4
     b = b+4
     c = c+4
     d = d+4

print ('='*50, '\n'*10)