#----- Importar biblioteca do Mysql
import MySQLdb
from model.endereco import Endereco

class EnderecoDb:
    #----- Configurar a conexão
    conexao = MySQLdb.connect(host='127.0.0.1',database='aulabd',user='root')
    #----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()
    
    def listar_todos(self):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = "SELECT * FROM endereço_pessoa"
        self.cursor.execute(comando_sql_select)
        #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        resultado = self.cursor.fetchall()
        lista_endereco_classe = self.converter_tabela_classe(resultado)
        return lista_endereco_classe

    def buscar_por_id(self, id):
            #----- Criação do comando SQL e passado para o cursor
            comando_sql_select = f"SELECT * FROM endereço_pessoa WHERE ID= {id}"
            self.cursor.execute(comando_sql_select)
            resultado = self.cursor.fetchone()
            return resultado

    def converter_tabela_classe(self, lista_tuplas):
        #cria uma lista para armazenar os dicionarios
        lista_endereco = []
        for e in lista_tuplas:
            #----- Criação do objeto da classe endereço
            e1 = Endereco()
            #--- pega cada posição da tupla e atribui a uma chave do dicionário
            e1.id = e[0]
            e1.logradouro = e[1]
            e1.numero= e[2]
            e1.complemento = e[3]
            e1.bairro = e[4]
            e1.cidade = e[5]
            lista_endereco.append(e1)
        return lista_endereco
