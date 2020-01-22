import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
import MySQLdb
from Model.squad_model import Squad

class SquadDao:
    conexao = MySQLdb.connect(host= '127.0.0.1', database= 'squads', user='root')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql = f"SELECT * FROM squad "
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM squad WHERE P.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando_sql = f""" INSERT INTO squad
        (
            NOME,
            DESCRICAO,
            NUMERO_PESSOAS,
            LINGUAGEM_BACKEND,
            FRAMEWORK_FRONTEND 
            )
            
        VALUES
        (
            '{squad.nome}',
            '{squad.descricao}',
            {squad.numero_pessoas},
            {squad.linguagem_BackEnd}
            {squad.framework_FrontEnd}
        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        novo_squad = self.cursor.lastrowid
        return novo_squad

    def alterar(self, squad:Squad):
        comando_sql = f""" UPDATE squad
        SET
            NOME = '{squad.nome}',
            DESCRICAO = {squad.descricao}
            NUMERO_PESSOAS ='{squad.numero_pessoas}',
            LINGUAGEM_BACKEND = {squad.linguagem_BackEnd},
            FRAMEWORK_FRONTEND = {squad.framework_FrontEnd}
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self, id):
        comando_sql = f"DELETE FROM squad WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()

# listar_todos(conexao, cursor)
# buscar_por_id(conexao, cursor, 1)