import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
from Dao.squad_dao import SquadDao
from Model.squad_model import Squad
from Dao.dao_frontend import FrontEndDao
from Model.model_frontend import FrontEnd

class FrontEndController:
    dao = FrontEndDao()
    model = FrontEnd()
    
    def listar_frontend(self):
        lista_frontend = []
        lista_tuplas = self.dao.listar_frontend()
        for s in lista_tuplas:
            squad = Squad()
            squad.id = s[0]
            squad.nome = s[1]
            lista_frontend.append(squad)
        return lista_frontend

    def buscar_id_frontend(self, id):
        s = self.dao.buscar_por_id(id)
        squad = Squad()
        squad.id = s[0]
        squad.nome = s[1]
        return squad

    def salvar_frontend(self, squad:Squad):
        return self.dao.salvar(squad)

    def alterar_frontend(self, squad:Squad):
        self.dao.alterar(squad)

    def deletar_frontend(self, id):
        self.dao.deletar(id)