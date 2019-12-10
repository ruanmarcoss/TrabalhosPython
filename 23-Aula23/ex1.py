dias_de_cada_mes = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

# qual_mes = int(input('Digite o número do mês (1..12): '))

# print('O mês', qual_mes, 'tem', dias_de_cada_mes[qual_mes], 'dias')

# print(f'Dias que faltam para acabar o ano, a partir do mês informado: {qual_mes} ')
# print(sum(list(dias_de_cada_mes.values())[qual_mes-1:]))

# total = 0 
# for mes in range(qual_mes,12+1):
#     total += dias_de_cada_mes[mes]
# print('modo estruturado')
# print('total de dias até o final do ano', total)

# for i in dias_de_cada_mes:
#     print('tenho uma chave na linha', i)
#     print('se tenho uma chave, tenho o valor', dias_de_cada_mes[i])

# for chave, valor in dias_de_cada_mes.items():
#     print('Para a chave', chave, 'o valor', valor)

tupla = ('text', 'texto de novo', 'textei', 'textatamento')

for isto in tupla:
    print(type(isto))
    print(isto)