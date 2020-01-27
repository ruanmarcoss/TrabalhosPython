import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
from Dao.dao_sgbds import SgbdsDao
from Model.model_sgbds import Sgbds
from Model.squad_model import Squad

class SgbdsController:
    dao = SgbdsDao()
    model = Sgbds()
    
    def listar_sgbds(self):
        lista_sgbds = []
        lista_tuplas = self.dao.listar_sgbds()
        for s in lista_tuplas:
            squad = Squad()
            squad.id = s[0]
            squad.nome = s[1]
            lista_sgbds.append(squad)
        return lista_sgbds

    def buscar_id_sgbds(self, id):
        s = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id = s[0]
        squad.nome = s[1]
        return squad

    def salvar_sgbds(self, squad:Squad):
        return self.dao.salvar_sgbds(squad)

    def alterar_sgbds(self, squad:Squad):
        self.dao.alterar_sgbds(squad)

    def deletar_sgbds(self, id):
        self.dao.deletar_sgbds(id)