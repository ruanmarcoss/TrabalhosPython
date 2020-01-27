import MySQLdb
import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
from Model.squad_model import Squad
from Model.model_backend import BackEnd
from Model.model_frontend import FrontEnd
from Model.model_sgbds import Sgbds
from Dao.dao_backend import BackEndDao
from Dao.dao_frontend import FrontEndDao
from Dao.dao_sgbds import SgbdsDao


class SquadDao:
    conexao = MySQLdb.connect(host= 'mysql.padawans.dev', database= 'padawans15', user='padawans15' , passwd='rd2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql = f"""SELECT 
                            s.id
                            ,s.nome
                            ,s.descricao
                            ,s.numero_pessoas
                            ,b.id
                            ,b.nome
                            ,f.id
                            ,f.nome
                            ,sg.id
                            ,sg.nome
                            FROM padawans15.cadastrosquad as s
                            right join fkbackend as b
                            on s.fk_linguagem_backend = b.id
                            right join fkfrontend as f
                            on s.fk_framework_frontend = f.id
                            right join fksgbds as sg
                            on s.fk_sgbds = sg.id; """
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self, id):
        comando = f"""SELECT 
                            s.id
                            ,s.nome
                            ,s.descricao
                            ,s.numero_pessoas
                            ,b.id
                            ,b.nome
                            ,f.id
                            ,f.nome
                            ,sg.id
                            ,sg.nome
                            FROM padawans15.cadastrosquad as s
                            right join fkbackend as b
                            on s.fk_linguagem_backend = b.id
                            right join fkfrontend as f
                            on s.fk_framework_frontend = f.id
                            right join fksgbds as sg
                            on s.fk_sgbds = sg.id;
                        WHERE ID = {id}"""
        # comando = f"SELECT * FROM cadastrosquad as C LEFT JOIN fkbackend as FKB on C.fk_linguagem_backend WHERE ID = {id}" \
        #                 " INNER JOIN fkfrontend as FKF on C.fk_framework_frontend WHERE ID = {id} " \
        #                 " INNER JOIN fksgbds as FKS on C.fk_sgbds WHERE ID = {id};"
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


if __name__ == "__main__":
    teste = SquadDao()
    print(teste.listar_todos())