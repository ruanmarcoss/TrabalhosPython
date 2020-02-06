from TrabalhosPython.Aula54.dao.squad_dao import SquadDao

dao = SquadDao()
squad = dao.list_all()
print(squad)
for s in squad:
    print(s)