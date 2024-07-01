from models.resultado import Resultado
from database import db

def create_resultado(data):
    resultado = Resultado(corrida_id=data['corrida_id'], piloto_id=data['piloto_id'], posicao=data['posicao'])
    db.session.add(resultado)
    db.session.commit()
    return resultado

def get_resultados():
    return Resultado.query.all()

def get_resultado_by_id(resultado_id):
    return Resultado.query.get(resultado_id)

def update_resultado(resultado_id, data):
    resultado = Resultado.query.get(resultado_id)
    if resultado:
        resultado.corrida_id = data['corrida_id']
        resultado.piloto_id = data['piloto_id']
        resultado.posicao = data['posicao']
        db.session.commit()
    return resultado

def delete_resultado(resultado_id):
    resultado = Resultado.query.get(resultado_id)
    if resultado:
        db.session.delete(resultado)
        db.session.commit()
