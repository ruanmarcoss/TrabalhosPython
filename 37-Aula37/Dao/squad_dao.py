import MySQLdb
from Model.squad_model import Squad

class SquadDao:
    conexao = MySQLdb.connect(host='127.0.0.1', database='squads', user='root')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando_sql_select = "SELECT * FROM squads"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall()
        lista_squad_classe = self.converter_tabela_classe(resultado)
        return lista_squad_classe

    def buscar_por_nome(self, nome):
        comando_sql_select = f"SELECT * FROM squads WHERE NOME = {nome}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado
    
    def salvar(self, squad:Squad):
        comando = f""" INSERT INTO squads
        (
            Nome,
            Descricao,
            Numero_Pessoas,
            Linguagem_BackEnd,
            Framework_FrontEnd
        )
        VALUES
        (
            '{squad.nome}',
            '{squad.descricao}',
            '{squad.numero_pessoas}',
            '{squad.linguagem_backend}',
            '{squad.framework_frontend}'
        )
        """
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squad:Squad):
        comando = f""" UPDATE squads
        SET
            Nome = '{squad.nome}',
            Descricao = '{squad.descricao}',
            NumeroPessoas = '{squad.numero_pessoas}',
            LinguagemBackEnd = '{squad.linguagem_backend}',
            FrameworkFrontEnd ='{squad.framework_frontend}'
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM squads WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()