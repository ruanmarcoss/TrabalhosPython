from flask_restful import Resource
from flask import request

from TrabalhosPython.Aula51.Model.endereco_model import EnderecoModel
from TrabalhosPython.Aula51.Dao.endereco_dao import EnderecoDao

class EnderecoController(Resource):#Fazendo herança na classe, usando o Resource
    def __init__(self):
        self.dao = EnderecoDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post(self):
        rua = request.json['rua']
        complemento = request.json['complemento']
        numero = int(request.json['numero'])
        cep = int(request.json['cep'])
        endereco = EnderecoModel(rua, complemento, numero, cep)
        comando = self.dao.insert(endereco)
        return comando

    def put(self, id):
        rua = request.json['rua']
        complemento = request.json['complemento']
        numero = int(request.json['numero'])
        cep = int(request.json['cep'])
        endereco = EnderecoModel(rua, complemento, numero, cep, id)
        comando = self.dao.update(endereco)
        return comando

    def delete(self, id):
        return self.dao.delete(id)