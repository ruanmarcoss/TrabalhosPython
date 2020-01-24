import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
import MySQLdb
from Model.squad_model import Squad

class SquadDao:
    conexao = MySQLdb.connect(host= 'mysql.padawans.dev', database= 'padawans15', user='padawans15' , passwd='rd2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql = f"SELECT * FROM cadastrosquad AS C LEFT JOIN fkbackend AS FKB ON C.fk_linguagem_backend = FKB.id \
                        SELECT * FROM cadastrosquad AS C LEFT JOIN fkfrontend AS FKB ON C.fk_framework_frontend = FKF.id \
                        SELECT * FROM cadastrosquad AS C LEFT JOIN sgbds AS FKB ON C.fk_sgbds = FKS.id"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self, id):
        comando = f"SELECT * FROM cadastrosquad WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando_sql = f""" INSERT INTO cadastrosquad
        (
            nome,
            descricao,
            numero_pessoas,
            fk_linguagem_backend,
            fk_framework_frontend,
            fk_sgbds 
            )
            
        VALUES
        (
            '{squad.nome}',
            '{squad.descricao}',
            {squad.numero_pessoas},
            {squad.fk_linguagem_backend},
            {squad.fk_framework_frontend},
            {squad.fk_sgbds}
        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        novo_squad = self.cursor.lastrowid
        return novo_squad

    def alterar(self, squad:Squad):
        comando_sql = f""" UPDATE cadastrosquad
        SET
            nome = '{squad.nome}',
            descricao = '{squad.descricao}',
            numero_pessoas = {squad.numero_pessoas},
            fk_linguagem_backend = {squad.fk_linguagem_backend},
            fk_framework_frontend = {squad.fk_framework_frontend},
            fk_sgbds = {squad.fk_sgbds}
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self, id):
        comando_sql = f"DELETE FROM cadastrosquad WHERE ID = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()

# listar_todos(conexao, cursor)
# buscar_por_id(conexao, cursor, 1)