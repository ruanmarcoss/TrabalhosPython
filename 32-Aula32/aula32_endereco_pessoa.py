# pip3 install flask_mysqldb
# referencia ao Mysql

import MySQLdb
#listar todas as pessoas 
def listar_todos(c):
    c.execute('SELECT * FROM endereço_pessoa')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)
        
#buscar uma pessoa pelo ID
def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM endereço_pessoa WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

#buscar pessoas por sobrenome
def buscar_por_logradouro(c, logradouro):
    c.execute(f"SELECT * FROM endereço_pessoa WHERE LOGRADOURO like '{logradouro}%' ")
    for p in c.fetchall():
        print(p)

#salvar pessoa
def salvar(cn, cr, logradouro, numero, complemento, bairro, cidade):
    cr.execute(f"INSERT INTO endereço_pessoa (LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, CIDADE )VALUES('{logradouro}', '{numero}','{complemento}','{bairro}','{cidade}')")
    cn.commit()

#alterar pessoa
def alterar(cn, cr, id, nome, sobrenome, idade, endereco_id='NULL'):
    cr.execute(f"UPDATE endereço_pessoa SET NOME='{nome}', SOBRENOME='{sobrenome}', IDADE={idade}, ENDERECO_ID={endereco_id} WHERE ID={id} ")
    cn.commit()

#deletar pessoa por ID
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM endereço_pessoa WHERE ID={id}')
    cn.commit()

conexao = MySQLdb.connect(host='127.0.0.1',database='aulabd',user='root')
cursor=conexao.cursor()

# listar_todos(cursor)
# buscar_por_id(cursor, 2)
# buscar_por_logradouro(cursor,'RUA')
salvar(conexao, cursor, 'RUA ', 'Perera', 51,2)
# alterar(conexao, cursor, 3, 'Cletim', 'Da Quebrada', 19, 2)
# deletar(conexao, cursor, 3)