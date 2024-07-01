from models.equipe import Equipe

def create_equipe(nome):
    from app import db  # Importando localmente
    nova_equipe = Equipe(nome=nome)
    db.session.add(nova_equipe)
    db.session.commit()
    return nova_equipe

def get_equipes():
    from app import db
    return Equipe.query.all()

def get_equipe_by_id(equipe_id):
    from app import db
    return Equipe.query.get(equipe_id)

def update_equipe(equipe_id, novo_nome):
    from app import db
    equipe = Equipe.query.get(equipe_id)
    if equipe:
        equipe.nome = novo_nome
        db.session.commit()
        return equipe
    return None

def delete_equipe(equipe_id):
    from app import db
    equipe = Equipe.query.get(equipe_id)
    if equipe:
        db.session.delete(equipe)
        db.session.commit()
        return True
    return False
