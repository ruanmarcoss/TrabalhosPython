import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
import MySQLdb
from Model.squad_model import Squad

def listar_frontend(self):
        comando_sql = f"SELECT * FROM fkfrontend"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado

def buscar_id_frontend(self, id):
        comando = f"SELECT * FROM fkfrontend WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

def salvar_frontend(self, squad:Squad):
        comando_sql = f""" INSERT INTO fkfrontend
        (nome)
            
        VALUES
        ('{squad.nome}')"""


def alterar_frontend(self, squad:Squad):
        comando_sql = f""" UPDATE fkfrontend
        SET
            nome = '{squad.nome}'
            
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

def deletar_frontend(self, id):
        comando_sql = f"DELETE FROM fkfrontend WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()