from models.corrida import Corrida
from database import db

def create_corrida(data):
    """
    Cria uma nova corrida.

    :param data: Dados da corrida a ser criada.
    :return: A corrida criada.
    """
    corrida = Corrida(nome=data['nome'], data=data['data_corrida'], pista_id=data['pista_id'])
    db.session.add(corrida)
    db.session.commit()
    return corrida

def get_corridas():
    """
    Retorna todas as corridas.

    :return: Lista de todas as corridas.
    """
    return Corrida.query.all()

def get_corrida_by_id(corrida_id):
    """
    Obtém uma corrida pelo seu identificador.

    :param corrida_id: Identificador da corrida.
    :return: A corrida correspondente ao identificador fornecido.
    """
    return Corrida.query.get(corrida_id)

def update_corrida(corrida_id, data):
    """
    Atualiza uma corrida existente.

    :param corrida_id: Identificador da corrida a ser atualizada.
    :param data: Dados atualizados da corrida.
    :return: A corrida atualizada.
    """
    corrida = Corrida.query.get(corrida_id)
    if corrida:
        corrida.nome = data['nome']
        corrida.data = data['data_corrida']
        db.session.commit()
    return corrida

def delete_corrida(corrida_id):
    """
    Deleta uma corrida pelo seu identificador.

    :param corrida_id: Identificador da corrida a ser deletada.
    """
    corrida = Corrida.query.get(corrida_id)
    if corrida:
        db.session.delete(corrida)
        db.session.commit()
