from models.equipe import Equipe

def create_equipe(nome):
    """
    Cria uma nova equipe.

    :param nome: Nome da nova equipe.
    :return: A equipe criada.
    """
    from app import db  # Importando localmente
    nova_equipe = Equipe(nome=nome)
    db.session.add(nova_equipe)
    db.session.commit()
    return nova_equipe

def get_equipes():
    """
    Retorna todas as equipes.

    :return: Lista de todas as equipes.
    """
    from app import db
    return Equipe.query.all()

def get_equipe_by_id(equipe_id):
    """
    Obtém uma equipe pelo seu identificador.

    :param equipe_id: Identificador da equipe.
    :return: A equipe correspondente ao identificador fornecido.
    """
    from app import db
    return Equipe.query.get(equipe_id)

def update_equipe(equipe_id, novo_nome):
    """
    Atualiza uma equipe existente.

    :param equipe_id: Identificador da equipe a ser atualizada.
    :param novo_nome: Novo nome da equipe.
    :return: A equipe atualizada.
    """
    from app import db
    equipe = Equipe.query.get(equipe_id)
    if equipe:
        equipe.nome = novo_nome
        db.session.commit()
        return equipe
    return None

def delete_equipe(equipe_id):
    """
    Deleta uma equipe pelo seu identificador.

    :param equipe_id: Identificador da equipe a ser deletada.
    :return: True se a equipe foi deletada, False caso contrário.
    """
    from app import db
    equipe = Equipe.query.get(equipe_id)
    if equipe:
        db.session.delete(equipe)
        db.session.commit()
        return True
    return False
