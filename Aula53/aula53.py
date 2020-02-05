#ORM
# ---- SqlAlchemy
# ---- Instalação do framework
# ---- pip3 install sqlalchemy

# ---- Conector do Mysql
# ---- Instalação do conector do Mysql
# ---- pip3 install mysql-connector-python

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class ProdutoModel(BaseModel):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=200))

    def __str__(self):
        return f"{self.id}-{self.nome}-{self.descricao}"

#----database+connector://user:passwd@url:porta/database
conexao = db.create_engine("mysql+mysqlconnector://root:@127.0.0.1:3306/produto")
criador_de_sessao = db.orm.sessionmaker()
criador_de_sessao.configure(bind=conexao)
sessao = criador_de_sessao()

produtos = sessao.query(ProdutoModel).all()
for p in produtos:
    print(p)
