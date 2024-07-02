from models.piloto import Piloto
from database import db

def create_piloto(data):
    """
    Cria um novo piloto.

    :param data: Dicionário contendo os dados do piloto.
    :return: O piloto criado.
    """
    piloto = Piloto(nome=data['nome'], idade=data['idade'], nacionalidade=data['nacionalidade'], equipe_id=data['equipe_id'])
    db.session.add(piloto)
    db.session.commit()
    return piloto

def get_pilotos():
    """
    Retorna todos os pilotos.

    :return: Lista de todos os pilotos.
    """
    return Piloto.query.all()

def get_piloto_by_id(piloto_id):
    """
    Obtém um piloto pelo seu identificador.

    :param piloto_id: Identificador do piloto.
    :return: O piloto correspondente ao identificador fornecido.
    """
    return Piloto.query.get(piloto_id)

def update_piloto(piloto_id, data):
    """
    Atualiza um piloto existente.

    :param piloto_id: Identificador do piloto a ser atualizado.
    :param data: Dicionário contendo os novos dados do piloto.
    :return: O piloto atualizado.
    """
    piloto = Piloto.query.get(piloto_id)
    if piloto:
        piloto.nome = data['nome']
        piloto.idade = data['idade']
        piloto.nacionalidade = data['nacionalidade']
        piloto.equipe_id = data['equipe_id']
        db.session.commit()
    return piloto

def delete_piloto(piloto_id):
    """
    Deleta um piloto pelo seu identificador.

    :param piloto_id: Identificador do piloto a ser deletado.
    """
    piloto = Piloto.query.get(piloto_id)
    if piloto:
        db.session.delete(piloto)
        db.session.commit()
