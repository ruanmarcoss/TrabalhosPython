import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37') # colocando o r na frente do endereço da pasta não é necessário mudar a barra
from Controller.squad_controller import SquadController
from Model.squad_model import Squad
from Model.squad_model import Squad
from Model.model_backend import BackEnd
from Model.model_frontend import FrontEnd
from Model.model_sgbds import Sgbds
from Dao.dao_backend import BackEnd
from Dao.dao_frontend import FrontEnd
from Dao.dao_sgbds import Sgbds

squad = Squad()
# squad.nome = 'Pdawan'
# squad.descricao = 'estagiários'
# squad.numero_pessoas = 40
# squad.linguagem_backend = 'Pyhton'
# squad.frameworkfrontend = 'django'

controller = SquadController()
print(controller.buscar_por_id(1))