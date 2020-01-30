"""""
from flask import Flask
from flask_restful import Api

from TrabalhosPython.Aula41.ambientevirtual.Controller.pessoa_controller import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/controller')

@app.route('/')
def inicio():
    return 'Bem vindo a controller'

app.run(debug=True, port=80)
"""""