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
<<<<<<< HEAD
                            join fkbackend as b
                            on s.fk_linguagem_backend = b.id
                            join fkfrontend as f
                            on s.fk_framework_frontend = f.id
                            join fksgbds as sg
                            on s.fk_sgbds = sg.id """
=======
                            left join fkbackend as b
                            on s.fk_linguagem_backend = b.id
                            left join fkfrontend as f
                            on s.fk_framework_frontend = f.id
                            left join fksgbds as sg
                            on s.fk_sgbds = sg.id; """
>>>>>>> d696271da183511b169fe42cb84e76b349e3e37d
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self, id):
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
                            join fkbackend as b
                            on s.fk_linguagem_backend = b.id
                            join fkfrontend as f
                            on s.fk_framework_frontend = f.id
                            sjoin fksgbds as sg
                            on s.fk_sgbds = sg.id
                        WHERE id = {id}"""
        self.cursor.execute(comando_sql)
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
        WHERE id = {squad.id}
        """
        self.cursor.execute(comando_sql)
        self.conexao.commit()

    def deletar(self, id):
        comando_sql = f"DELETE FROM cadastrosquad WHERE id = {id}"
        self.cursor.execute(comando_sql)
        self.conexao.commit()

# listar_todos(conexao, cursor)
<<<<<<< HEAD
# buscar_por_id(conexao, cursor, 1)


# if __name__ == "__main__":
#     teste = SquadDao()
#     print(teste.listar_todos())
=======
# buscar_por_id(conexao, cursor, 1)
>>>>>>> d696271da183511b169fe42cb84e76b349e3e37d
