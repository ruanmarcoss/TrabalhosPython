from TrabalhosPython.Aula54.dao.base_dao import BaseDao
from TrabalhosPython.Aula54.model.squad_model import SquadModel

class SquadDao(BaseDao):
    def list_all(self):
        return self.sessao.query(SquadModel).all()
