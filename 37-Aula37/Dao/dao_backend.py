import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
import MySQLdb
from Model.squad_model import Squad

def listar_backend(self):
        comando_sql = f"SELECT * FROM fkbackend"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado

def buscar_id_backend(self, id):
        comando = f"SELECT * FROM fkbackend WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

def salvar_backend(self, squad:Squad):
        comando_sql = f""" INSERT INTO fkbackend
        (nome)
            
        VALUES
        ('{squad.nome}')"""
        

def alterar_backend(self, squad:Squad):
        comando_sql = f""" UPDATE fkbackend
        SET
            nome = '{squad.nome}'
            
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

def deletar_backend(self, id):
        comando_sql = f"DELETE FROM fkbackend WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()