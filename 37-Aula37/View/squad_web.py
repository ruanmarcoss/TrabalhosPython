from flask import Flask, render_template, request, redirect
import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
from Controller.squad_controller import SquadController
from Model.squad_model import Squad

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
    if id_squad != 'None':
        squad_controller.deletar(id_squad)
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squad = Squad()
    squad.id = request.args['id']
    squad.nome = request.args['nome']
    squad.descricao = request.args['descricao']
    squad.numero_pessoas = request.args['numero_pessoas']
    squad.linguagem_backend = request.args ['linguagem_backend']
    squad.framework_frontend = request.args ['framework_frontend']
  
#     pessoa.endereco = end
#     if pessoa.id == 0:
#         pessoa_controller.salvar(pessoa)
#     else:
#         pessoa_controller.alterar(pessoa)
#     return redirect('/listar')

app.run(debug=True)