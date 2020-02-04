import MySQLdb
from TrabalhosPython.Aula51.Model.endereco_model import EnderecoModel

class EnderecoDao:
    def __init__(self):
        self.conexao = MySQLdb.connect(host='127.0.0.1',database='endereco',user='root',passwd='')
        self.cursor = self.conexao.cursor()

    def list_all(self):
        self.cursor.execute("SELECT * FROM endereco")
        endereco = self.cursor.fetchall()
        lista_endereco = []
        for e in endereco:
            end = EnderecoModel(e[1],e[2],e[3],e[4],e[0])
            lista_endereco.append(end.__dict__)
        return lista_endereco

    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM endereco WHERE ID = {id}")
        endereco = self.cursor.fetchone()
        e = EnderecoModel(endereco[1], endereco[2], endereco[3], endereco[4], endereco[0])
        return e.__dict__

    def insert(self, endereco : EnderecoModel):
        self.cursor.execute(f"""INSERT INTO endereco
        (rua, complemento, numero, cep)
        VALUES
        ('{endereco.rua}',
        '{endereco.complemento}',
        {endereco.numero},
        {endereco.cep})
        """)
        self.conexao.commit()
        id = self.cursor.lastrowid
        endereco.id = id
        return endereco.__dict__

    def update(self, endereco : EnderecoModel):
        self.cursor.execute(f"""
                UPDATE endereco 
                    SET 
                        rua = '{endereco.rua}',
                        complemento = '{endereco.complemento}',
                        numero = {endereco.numero},
                        cep = {endereco.cep}
                    WHERE ID = {endereco.id}
             """)
        self.conexao.commit()
        return endereco.__dict__

        # self.cursor.execute(f""""
        # UPDATE endereco
        #     SET
        #         rua = '{endereco.rua}',
        #         complemento = '{endereco.complemento}',
        #         numero = {endereco.numero},
        #         cep = {endereco.cep},
        #     WHERE ID = {endereco.id}
        #         """)
        # self.conexao.commit()
        # return endereco.__dict__

    def delete(self, id):
        self.cursor.execute(f"DELETE FROM endereco WHERE ID = {id}")
        self.conexao.commit()
        return f"Removido o endereco de id = {id}"