from models.corrida import Corrida
from database import db

def create_corrida(data):
    corrida = Corrida(nome=data['nome'], data=data['data_corrida'], pista_id=data['pista_id'])
    db.session.add(corrida)
    db.session.commit()
    return corrida

def get_corridas():
    return Corrida.query.all()

def get_corrida_by_id(corrida_id):
    return Corrida.query.get(corrida_id)

def update_corrida(corrida_id, data):
    corrida = Corrida.query.get(corrida_id)
    if corrida:
        corrida.nome = data['nome']
        corrida.data = data['data_corrida']
        db.session.commit()
    return corrida

def delete_corrida(corrida_id):
    corrida = Corrida.query.get(corrida_id)
    if corrida:
        db.session.delete(corrida)
        db.session.commit()
