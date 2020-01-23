from flask import Flask, render_template, request, redirect
import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
from Controller.squad_controller import SquadController
from Model.squad_model import Squad
from Dao.squad_dao import SquadDao

app = Flask(__name__)
squad_controller = SquadController()
nome = 'Cadastros Squad'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squad = squad_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = squad)

@app.route('/cadastrar')
def cadastrar():
    squad = Squad()
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
    squad.Id = int(request.args['Id'])
    squad.Nome = request.args['Nome']
    squad.Descricao = request.args['Descricao']
    squad.NumeroPessoas = request.args['NumeroPessoas']
    squad.LinguagemBackEnd = request.args['LinguagemBackEnd']
    squad.FrameWorkFrontEnd = request.args['FrameworkFrontEnd']
    
  
    if squad.Id == 0:
        squad_controller.salvar(squad)
    else:
        squad_controller.alterar(squad)
    return redirect('/listar')

app.run(debug=True)