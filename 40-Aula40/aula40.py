#Flask RestFul
#GET, POST, PUT, DELETE/ São métodos http.
from flask import Flask
from flask_restful import Api
from Controllers.cerveja_controller import CervejaController
"""
app = Flask(__name__)
api = Api(app)

api.add_resource(CervejaController, '/api/cerveja')

@app.route('/')
def inicio():

    return'Bem vindo a API'

    return 'Bem vindo a Api'


app.run(debug=True, port=80)

"""