"""""
from flask_restful import Resource

from Dao.pessoa_dao import PessoaDao

class PessoaController(Resource):#Utilizando o Resource como argumento, está fazendo uma herença na classe
    def __init__(self):
        self.dao = PessoaDao()

    def get(self):
        msg = self.dao.list_all()
        return msg

    def post(self):
        msg = self.dao.insert('')
        return msg

    def put(self):
        msg = self.dao.update('')
        return msg

    def delete(self):
        msg = self.dao.remove(10)
        return msg
"""""