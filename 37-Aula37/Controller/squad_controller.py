import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
from Dao.squad_dao import SquadDao
from Model.squad_model import Squad
from Model.model_backend import BackEnd
from Model.model_frontend import FrontEnd
from Model.model_sgbds import Sgbds
from Dao.dao_backend import BackEndDao
from Dao.dao_frontend import FrontEndDao
from Dao.dao_sgbds import SgbdsDao

class SquadController:
    dao = SquadDao()
    model = Squad()
    # backend = BackEndDao()
    # frontend= FrontEndDao()
    # sgbds = SgbdsDao()
    # backend_model = BackEnd()
    # frontend_model = FrontEnd()
    # sgbds_model = Sgbds()
    
    def listar_todos(self):
        lista_squad = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            squad = Squad()
            squad.id = s[0]
            squad.nome = s[1]
            squad.descricao = s[2]
            squad.numero_pessoas = s[3]
            squad.fk_linguagem_backend.id = s[4]
            squad.fk_framework_frontend.id = s[5]
            squad.fk_sgbds.id = s[6]
            lista_squad.append(squad)
        return lista_squad

    def buscar_por_id(self, id):
        s = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id = s[0]
        squad.nome = s[1]
        squad.descricao = s[2]
        squad.numero_pessoas = s[3]
        squad.fk_linguagem_backend.id = s[4]
        squad.fk_linguagem_backend.nome = s[5]
        return squad

    def salvar(self, squad:Squad):
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        self.dao.alterar(squad)

    def deletar(self, id):
        self.dao.deletar(id)