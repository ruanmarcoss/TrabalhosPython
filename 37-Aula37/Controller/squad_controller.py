from Dao.squad_dao import SquadDao
from Model.squad_model import Squad

class SquadController:
    dao = SquadDao()
    model = Squad()

    def listar_todos(self):
        lista_squad = []