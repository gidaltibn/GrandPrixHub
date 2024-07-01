from models.pista import Pista
from database import db

def create_pista(data):
    pista = Pista(nome=data['nome'], pais=data['pais'])
    db.session.add(pista)
    db.session.commit()
    return pista

def get_pistas():
    return Pista.query.all()

def get_pista_by_id(pista_id):
    return Pista.query.get(pista_id)

def update_pista(pista_id, data):
    pista = Pista.query.get(pista_id)
    if pista:
        pista.nome = data['nome']
        pista.pais = data['pais']
        db.session.commit()
    return pista

def delete_pista(pista_id):
    pista = Pista.query.get(pista_id)
    if pista:
        db.session.delete(pista)
        db.session.commit()
