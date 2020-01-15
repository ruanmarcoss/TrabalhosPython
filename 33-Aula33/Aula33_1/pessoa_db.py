#----- Importar biblioteca do Mysql
import MySQLdb

def listar_todos():
    #----- Configurar a conexão
    conexao = MySQLdb.connect(host='127.0.0.1',database='aulabd',user='root')
    cursor = conexao.cursor()
    #----- Criação do comando SQL e passado para o cursor
    comando_sql_select = "SELECT * FROM pessoa"
    cursor.execute(comando_sql_select)
    #----- Pega todos os resultados da execução do comando SQL e armezana em uma variável
    resultado = cursor.fetchall()
    return resultado