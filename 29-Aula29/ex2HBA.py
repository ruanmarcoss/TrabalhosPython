el1='Piloto'
el2='Oficial 1'
el3='Oficial 2'
el4='chefe de serviço de voo'
el5='comissária 1'
el6='comissária 2'
el7='Bandido'
el8='Policial'
carro = []
aviao = []
terminal = [el1,el2,el3,el4,el5,el6,el7,el8]
numero_viagem=0

def viagem_fortwo():
    global numero_viagem
    numero_viagem += 1
    print(f'\n========== Viagem {numero_viagem} ==========')
    print(f'Estão no terminal: {terminal}')

def viagem():
    viagem_fortwo()
    terminal.remove(el4)
    terminal.remove(el5)
    carro.append(el4)
    carro.append(el5)
    print(f'A {el5} e o {el4} embarcaram no Fortwo e vão até o avião')
    carro.remove(el5)
    aviao.append(el5)
    print(f'A {el5} desce do Fortwo e embarca no avião ')
    print(f'Estão no avião: {aviao}')
    print(f'O {el4} volta no Fortwo para o terminal')
    
def viagem2():
    terminal.append(el4)
    viagem_fortwo()
    terminal.remove(el4)
    terminal.remove(el6)
    carro.append(el6)
    print(f'A {el6} embarca no Fortwo com o {el4} e vão até o avião')
    carro.remove(el6)
    aviao.append(el6)
    print(f'A {el6} desce do Fortwo e embarca no avião')
    print(f'Estão no avião: {aviao}')
    print(f'O {el4} volta no Fortwo para o terminal')

def viagem3():
    carro.remove(el4)
    terminal.append(el4)
    print(f'O {el4} desce do Fortwo e fica no terminal')
    viagem_fortwo()
    terminal.remove(el1)
    terminal.remove(el2)
    carro.append(el1)
    carro.append(el2)
    print(f'{el1} e {el2} entram no Fortwo e vão até o avião')
    carro.remove(el2)
    aviao.append(el2)
    print(f'O {el2} desce do Fortwo e entra no avião')
    print(f'Estão no avião: {aviao}')
    print(f'O {el1} volta no Fortwo para o terminal')

def viagem4():
    terminal.append(el1)
    viagem_fortwo()
    terminal.remove(el3)
    terminal.remove(el1)
    carro.append(el3)
    print(f'{el3} entra no Fortwo com o {el1} e vão até o avião')
    carro.remove(el3)
    aviao.append(el3)
    print(f'O {el3} entra no avião')
    print(f'Estão no avião: {aviao}')
    print(f'O {el1} volta no Fortwo para o terminal')

def viagem5():
    terminal.append(el1)
    viagem_fortwo()
    terminal.remove(el4)
    terminal.remove(el1)
    carro.append(el4)
    print(f'{el4} entra no Fortwo com o {el1} e vão até o avião')
    carro.remove(el4)
    aviao.append(el4)
    print(f'O {el4} entra no avião')
    print(f'Estão no avião: {aviao}')
    print(f'O {el1} volta no Fortwo para o terminal')

def viagem6():
    terminal.append(el1)
    carro.remove(el1)
    print(f'O {el1} sai do fortwo e fica no terminal')
    viagem_fortwo()
    terminal.remove(el7)
    terminal.remove(el8)
    carro.append(el8)
    carro.append(el7)
    print(f'O {el7} e o {el8} entram no fortwo e vão até o avião')
    carro.remove(el7)
    carro.remove(el8)
    aviao.append(el8)
    aviao.append(el7)
    print(f'O {el7} e o {el8} saem do fortwo e entram no avião')
    aviao.remove(el4)
    print(f'O {el4} sai do avião e volta com o fortwo para o terminal')
    print(f'Estão no avião: {aviao}')

def viagem7():
    terminal.append(el4)
    viagem_fortwo()
    terminal.remove(el1)
    terminal.remove(el4)
    carro.append(el1)
    carro.append(el4)
    print(f'{el1} entra no Fortwo com o {el4} e vão até o avião')
    carro.remove(el1)
    carro.remove(el4)
    aviao.append(el1)
    aviao.append(el4)
    print(f'O {el1} e o {el1} entram no avião')
    print(f'Estão no avião: {aviao}')

viagem()
viagem2()
viagem3()
viagem4()
viagem5()
viagem6()
viagem7()
