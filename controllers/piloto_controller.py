from models.piloto import Piloto
from database import db

def create_piloto(data):
    piloto = Piloto(nome=data['nome'], idade=data['idade'], nacionalidade=data['nacionalidade'], equipe_id=data['equipe_id'])
    db.session.add(piloto)
    db.session.commit()
    return piloto

def get_pilotos():
    return Piloto.query.all()

def get_piloto_by_id(piloto_id):
    return Piloto.query.get(piloto_id)

def update_piloto(piloto_id, data):
    piloto = Piloto.query.get(piloto_id)
    if piloto:
        piloto.nome = data['nome']
        piloto.idade = data['idade']
        piloto.nacionalidade = data['nacionalidade']
        db.session.commit()
    return piloto

def delete_piloto(piloto_id):
    piloto = Piloto.query.get(piloto_id)
    if piloto:
        db.session.delete(piloto)
        db.session.commit()
