import MySQLdb
import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
from Model.squad_model import Squad
from Model.model_sgbds import Sgbds

class SgbdsDao:
        conexao = MySQLdb.connect(host= 'mysql.padawans.dev', database= 'padawans15', user='padawans15' , passwd='rd2019')
        cursor = conexao.cursor()
        
        def listar_sgbds(self):
                comando_sql = f"SELECT * FROM fksgbds"
                self.cursor.execute(comando_sql)
                resultado = self.cursor.fetchall()
                return resultado

        def buscar_id_sgbds(self, id):
                comando = f"SELECT * FROM fksgbds WHERE ID = {id}"
                self.cursor.execute(comando)
                resultado = self.cursor.fetchone()
                return resultado

        def salvar_sgbds(self, squad:Squad):
                comando_sql = f""" INSERT INTO fksgbds
                (nome)
                
                VALUES
                ('{squad.nome}')"""

                self.cursor.execute(comando_sql)
                self.conexao.commit()
                novo_squad = self.cursor.lastrowid
                return novo_squad

        def alterar_sgbds(self, squad:Squad):
                comando_sql = f""" UPDATE fksgbds
                SET
                nome = '{squad.nome}'

                WHERE ID = {squad.id}
                """
                self.cursor.execute(comando_sql)
                self.conexao.commit()

        def deletar_sgbds(self, id):
                comando_sql = f"DELETE FROM fksgbds WHERE ID = {id}"
                self.cursor.execute(comando_sql)
                self.conexao.commit()