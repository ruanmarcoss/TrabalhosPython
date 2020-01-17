from flask import Flask, render_template
import sys
sys.path.append('/Users/900160/Documents/TrabalhosPython/TrabalhosPython/33-Aula33_/Aula33-4')
from controller.pessoa_controller import PessoaController
from controller.endereco_controller import EnderecoController
app = Flask(__name__)
pc = PessoaController()
ec = EnderecoController()

@app.route('/')
def inicio():
    pessoas = pc.listar_todos()
    enderecos = ec.listar_todos()
    return render_template('index.html', lista = pessoas, endereco = enderecos)

app.run()