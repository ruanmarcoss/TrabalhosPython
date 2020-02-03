from flask import Flask
from flask_restful import Api

from TrabalhosPython.Aula41.Controller.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/controller', endpoint='pessoas')
api.add_resource(PessoaController, '/api/controller/<int:id>', endpoint='pessoa')

@app.route('/')
def inicio():
    return 'Teste api '

app.run(debug=True, port=80)