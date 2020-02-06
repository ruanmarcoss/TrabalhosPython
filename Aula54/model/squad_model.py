import  sqlalchemy as db

from sqlalchemy.ext.declarative import declarative_base

BaseAlchemy = declarative_base()

class SquadModel(BaseAlchemy):
    __tablename__ = 'squad'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=45))
    descricao = db.Column(db.String(length=45))
    numero = db.Column(db.String(length=45))
    backend = db.Column(db.String(length=45))
    frontend = db.Column(db.String(length=45))

    def __str__(self):
        return f"{self.id},{self.nome},{self.descricao},{self.numero},{self.backend},{self.frontend}"