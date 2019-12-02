# Aula 17 02/12/2019
# Dicionário, While

# bole = True
n = 0
# while n >= 30:
#     n = n +1
#     print(f'Fala tropinha {n}')

# while False:
#     n = n +1
#     print(f'Fala tropinha {n}')

# while n <= 30:
#     n = n +1
#     print(f'Fala tropinha {n}')
#     break
#     print(f'Passou!')

# while n <= 30:
#     n = n +1
#     print(f'Fala tropinha {n}')
#     continue # Linhas abaixo da função não serão executados
#     print(f'Passou!')

while n <= 30:
    n = n +1
    print(f'Fala tropinha {n}')
    if n == 10:
        continue
    print(f'Passou!')

    