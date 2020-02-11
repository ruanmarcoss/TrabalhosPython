import sqlalchemy as db
from sqlalchemy.orm import relationship

from TrabalhosPython.Aula55.model.pessoa import Pessoa
from TrabalhosPython.Aula55.model.base import Base
from TrabalhosPython.Aula55.dao.pessoa_dao import PessoaDao

class Autor(Base):
    __tablename__ = "LIVRARIA_AUTOR"
    id = db.Column(db.Integer, primary_key=True)
    pseudonimo = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=200))
    pessoa_id = db.Column(db.Integer, db.ForeignKey('LIVRARIA_PESSOA.id'))
    pessoa = relationship(Pessoa)

    def __init__(self, id, pseudonimo, descricao, pessoa_id, pessoa):
        self.id = id
        self.pseudonimo = pseudonimo
        self.descricao = descricao
        self.pessoa_id = pessoa_id
        self.pessoa = pessoa

    def __str__(self):
        return f"{self.id};{self.pseudonimo};{self.descricao};{self.pessoa_id};{self.pessoa}"

