from models.pista import Pista
from database import db

def create_pista(data):
    """
    Cria uma nova pista.

    :param data: Dicionário contendo os dados da pista.
    :return: A pista criada.
    """
    pista = Pista(nome=data['nome'], pais=data['pais'])
    db.session.add(pista)
    db.session.commit()
    return pista

def get_pistas():
    """
    Retorna todas as pistas.

    :return: Lista de todas as pistas.
    """
    return Pista.query.all()

def get_pista_by_id(pista_id):
    """
    Obtém uma pista pelo seu identificador.

    :param pista_id: Identificador da pista.
    :return: A pista correspondente ao identificador fornecido.
    """
    return Pista.query.get(pista_id)

def update_pista(pista_id, data):
    """
    Atualiza uma pista existente.

    :param pista_id: Identificador da pista a ser atualizada.
    :param data: Dicionário contendo os novos dados da pista.
    :return: A pista atualizada.
    """
    pista = Pista.query.get(pista_id)
    if pista:
        pista.nome = data['nome']
        pista.pais = data['pais']
        db.session.commit()
    return pista

def delete_pista(pista_id):
    """
    Deleta uma pista pelo seu identificador.

    :param pista_id: Identificador da pista a ser deletada.
    """
    pista = Pista.query.get(pista_id)
    if pista:
        db.session.delete(pista)
        db.session.commit()
