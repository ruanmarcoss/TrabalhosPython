import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
from Dao.squad_dao import SquadDao
from Model.squad_model import Squad
from Dao.dao_backend import BackEndDao
from Model.model_backend import BackEnd

class BackEndController:
    dao = BackEndDao()
    model = BackEnd()
    
    def listar_backend(self):
        lista_backend = []
        lista_tuplas = self.dao.listar_backend()
        for s in lista_tuplas:
            squad = Squad()
            squad.id = s[0]
            squad.nome = s[1]
            lista_backend.append(squad)
        return lista_backend

    def buscar_id_backend(self, id):
        s = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id = s[0]
        squad.nome = s[1]
        return squad

    def salvar_backend(self, squad:Squad):
        return self.dao.salvar_backend(squad)

    def alterar_backend(self, squad:Squad):
        self.dao.alterar_backend(squad)

    def deletar_backend(self, id):
        self.dao.deletar_backend(id)