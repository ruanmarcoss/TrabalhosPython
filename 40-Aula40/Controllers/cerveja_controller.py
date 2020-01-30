from flask_restful import Resource

class CervejaController(Resource):
    def get(self):
        return 'Acessando controlador via HTTP GET'

    def post(self):
        return 'Acessando controlador via HTTP POST'

    def put(self):
        return 'Acessando controlador via HTTP PUT'

    def delete(self):
        return 'Acessando controlador via HTTP DELETE'