# REFERÊNCIA O MySQL
import MySQLdb

def listar_todos(c):
    c.execute('SELECT * FROM pessoa')
    pessoas = c.fetchall()
    for p in pessoas:
        print(p)

def buscar_por_id(c,id):
    c.execute(f'SELECT * FROM pessoa WHERE id = {id}')
    pessoas = c.fetchone()
    print(pessoas)


conexao = MySQLdb.connect(host='127.0.0.1',database='aulabd',user='root')
cursor=conexao.cursor()
listar_todos(cursor)
buscar_por_id(cursor,1)



