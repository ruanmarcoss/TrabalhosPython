from flask import Flask, render_template, request, redirect
import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
from Controller.squad_controller import SquadController
from Controller.backend_controller import BackEndController
from Controller.frontend_controller import FrontEndController
from Controller.sgbds_controller import SgbdsController
from Model.squad_model import Squad
from Dao.squad_dao import SquadDao
from Model.model_backend import BackEnd
from Model.model_frontend import FrontEnd
from Model.model_sgbds import Sgbds
from Dao.dao_backend import BackEndDao
from Dao.dao_frontend import FrontEndDao
from Dao.dao_sgbds import SgbdsDao



app = Flask(__name__)
squad_controller = SquadController()
backend_controller = BackEndController()
frontend_controller = FrontEndController()
sgbds_controller = SgbdsController()
nome = 'Cadastros Squad'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squad = squad_controller.listar_todos()
    backend = backend_controller.listar_backend()
    frontend = frontend_controller.listar_frontend()
    sgbds = sgbds_controller.listar_sgbds()
    return render_template('listar.html', titulo_app = nome, lista = squad)

@app.route('/cadastrar')
def cadastrar():
    squad = Squad()
    backend = BackEnd()
    frontend = FrontEnd()
    sgbds = Sgbds()
    if 'id' in request.args:
        id = request.args['id']
        squad = squad_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, squad = squad)


@app.route('/excluir')
def excluir():
    id = int(request.args['id'])
    squad_controller.deletar(id)
    if id != 'None':
        squad_controller.deletar(id)
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squad = Squad()
    squad.id = int(request.args['id'])
    squad.nome = request.args['nome']
    squad.descricao = request.args['descricao']
    squad.numero_pessoas = int(request.args['numero_pessoas'])
    squad.fk_linguagem_backend = (request.args['fk_linguagem_backend.nome'])
    squad.fk_framework_frontend = (request.args['fk_framework_frontend.nome'])
    squad.fk_sgbds = (request.args['fk_sgbds.nome'])
    
  
    if squad.id == 0:
        squad_controller.salvar(squad)
    else:
        squad_controller.alterar(squad)
    return redirect('/listar')

app.run(debug=True)
