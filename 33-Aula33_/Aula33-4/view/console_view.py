import sys
sys.path.append('/Users/900160/Documents/TrabalhosPython/TrabalhosPython/33-Aula33_/Aula33-4')
from controller.pessoa_controller import PessoaController
from controller.endereco_controller import EnderecoController
pc = PessoaController()
ec = EnderecoController()

for p in pc.listar_todos():
    print(p)

for e in ec.listar_todos():
    print(e)