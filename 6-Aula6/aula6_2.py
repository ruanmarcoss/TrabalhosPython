# Aula 6 - P2 - 13-11-2019
# Estruturas de repetição - FOR


# ---- for simples usando range com incremento padrão de 1
for i in range (0,10):
    print(f'{i}-Padawans Hbpy')

# ---- for usando range com incremento de 2
for i in range(0,100,2):
    print(f'{i}- Pares')


#---- for em lista range
lista = ['Mateus' , 'Matheus' , 'Marcela' , 'Nicole' , 'Tonho' , 'Pablo']
for i in range(0,6):
    print(lista[i])

#---- exemplificando o problema do uso de for em lista usando range
lista.append('Natan') 
for sortudo in lista:
    print(sortudo)

#---- for usando os elementos da própria lista
número = 10
for i in range(0,11):
    print(f'{i} x {número} = {i*número}')
