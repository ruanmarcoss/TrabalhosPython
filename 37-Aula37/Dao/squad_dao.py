import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
import MySQLdb
from Model.squad_model import Squad

class SquadDao:
    conexao = MySQLdb.connect(host= '127.0.0.1', database= 'squads', user='root')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql = f"SELECT * FROM squad"
        self.cursor.execute(comando_sql)
        resultado = self.cursor.fetchall()
        return resultado
        
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM squad WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando_sql = f""" INSERT INTO squad
        (
            Nome,
            Descricao,
            NumeroPessoas,
            LinguagemBackEnd,
            FrameWorkFrontEnd 
            )
            
        VALUES
        (
            '{squad.Nome}',
            '{squad.Descricao}',
            {squad.NumeroPessoas},
            '{squad.LinguagemBackEnd}',
            '{squad.FrameWorkFrontEnd}'
        )"""
        self.cursor.execute(comando_sql)
        self.conexao.commit()
        novo_squad = self.cursor.lastrowid
        return novo_squad

    def alterar(self, squad:Squad):
        comando_sql = f""" UPDATE squad
        SET
            Nome = '{squad.Nome}'
            Descricao = '{squad.Descricao}'
            NumeroPessoas = {squad.NumeroPessoas}
            LinguagemBackEnd = '{squad.LinguagemBackEnd}'
            FrameWorkFrontEnd  = '{squad.FrameWorkFrontEnd}'
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