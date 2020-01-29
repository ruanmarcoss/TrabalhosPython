from flask_restful import Resource


class CervejaController(Resource):
    def get(self):
        return 'Acessando a controladora pelo HTTP GET'
    def post(self):
        return 'Acessando a controladora pelo HTTP POST'
    def put(self):
        return 'Acessando a controladora pelo HTTP PUT'
    def delete(self):
        return 'Acessando a controladora pelo HTTP DELETE'