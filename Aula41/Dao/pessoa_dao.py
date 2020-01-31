import MySQLdb
from TrabalhosPython.Aula41.Model.pessoa_model import PessoaModel


class PessoaDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.dev',database='topskills01',user='topskills01',passwd='ts2019')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute("SELECT * FROM 01_MDG_PESSOA")
        pessoas = self.cursor.fetchall()
        lista_pessoa = []
        for p in pessoas:
            pessoa = PessoaModel(p[1], p[2], p[3], p[0])
            lista_pessoa.append(pessoa.__dict__)
        return lista_pessoa

    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM 01_MDG_PESSOA WHERE ID = {id}")
        pessoa = self.cursor.fetchone()
        p = PessoaModel(pessoa[1], pessoa[2], pessoa[3], pessoa[0])
        return p.__dict__

    def insert(self, pessoa):
        return f'Cadastrando uma pessoa : {pessoa}'

    def update(self, pessoa):
        return f'Alterando uma pessoa : {pessoa}'

    def delete(self, id):
        self.cursor.execute(f"DELETE FROM 01_MDG_PESSOA WHERE ID = {id}")
        self.connection.commit()
        return 'A pessoa foi deletada com sucesso'

