import sys
sys.path.append(r'C:\Users\900160\Documents\TrabalhosPython\TrabalhosPython\37-Aula37')
from Dao.squad_dao import SquadDao
from Model.squad_model import Squad

class BackEndController:
    dao = SquadDao()
    model = Squad()
    
    def listar_todos(self):
        lista_backend = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            squad = Squad()
            squad.id = s[0]
            squad.nome = s[1]
            lista_backend.append(squad)
        return lista_backend