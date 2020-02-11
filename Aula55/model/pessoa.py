import sqlalchemy as db

from TrabalhosPython.Aula55.model.base import Base

class Pessoa(Base):
    __tablename__ = 'LIVRARIA_PESSOA'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    sobrenome = db.Column(db.String(length=100))
    # data_nascimento = db.Column(db.DATE)
    naturalidade = db.Column(db.String(length=100))

    def __init__(self, id, nome, sobrenome, data_nascimento, naturalidade):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        # self.data_nascimento = data_nascimento
        self.naturalidade = naturalidade

    def __str__(self):
        return f"{self.id};{self.nome};{self.sobrenome};{self.naturalidade}"
