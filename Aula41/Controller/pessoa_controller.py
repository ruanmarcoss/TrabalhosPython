from flask_restful import Resource

from TrabalhosPython.Aula41.Dao.pessoa_dao import PessoaDao

class PessoaController(Resource):#Utilizando o Resource como argumento, está fazendo uma herença na classe
    def __init__(self):
        self.dao = PessoaDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post(self):
        msg = self.dao.insert('')
        return msg

    def put(self):
        msg = self.dao.update('')
        return msg

    def delete(self):
        msg = self.dao.delete()
        return msg
