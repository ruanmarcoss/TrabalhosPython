# pip3 install flask_mysqldb
# referencia ao Mysql

import MySQLdb
#listar todas as pessoas 
def listar_todos(c):
    c.execute('SELECT * FROM pessoa')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)
        
#buscar uma pessoa pelo ID
def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM pessoa WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

#buscar pessoas por sobrenome
def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM pessoa WHERE SOBRENOME like '{sobrenome}%' ")
    for p  in  c.fetchall():
        print(p)

#salvar pessoa
def salvar(cn, cr, nome, sobrenome, idade, endereco_id='NULL'):
    cr.execute(f"INSERT INTO pessoa (NOME, SOBRENOME, IDADE, ENDERECO_ID )VALUES('{nome}', '{sobrenome}',{idade},{endereco_id})")
    cn.commit()

#alterar pessoa
def alterar(cn, cr, id, nome, sobrenome, idade, endereco_id='NULL'):
    cr.execute(f"UPDATE pessoa SET NOME='{nome}', SOBRENOME='{sobrenome}', IDADE={idade}, ENDERECO_ID={endereco_id} WHERE ID={id} ")
    cn.commit()

#deletar pessoa por ID
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM pessoa WHERE ID={id}')
    cn.commit()

conexao = MySQLdb.connect(host='127.0.0.1',database='aulabd',user='root')
cursor=conexao.cursor()

# listar_todos(cursor)
# buscar_por_id(cursor, 1)
# buscar_por_sobrenome(cursor,'da')
# salvar(conexao, cursor, 'Cleyton', 'Perera', 51,2)
# alterar(conexao, cursor, 3, 'Cletim', 'Da Quebrada', 19, 2)
# deletar(conexao, cursor, 3)