from models.resultado import Resultado
from database import db

def create_resultado(data):
    """
    Cria um novo resultado.

    :param data: Dicionário contendo os dados do resultado.
    :return: O resultado criado.
    """
    resultado = Resultado(
        corrida_id=data['corrida_id'],
        piloto_id=data['piloto_id'],
        posicao=data['posicao']
    )
    db.session.add(resultado)
    db.session.commit()
    return resultado

def get_resultados():
    """
    Retorna todos os resultados.

    :return: Lista de todos os resultados.
    """
    return Resultado.query.all()

def get_resultado_by_id(resultado_id):
    """
    Obtém um resultado pelo seu identificador.

    :param resultado_id: Identificador do resultado.
    :return: O resultado correspondente ao identificador fornecido.
    """
    return Resultado.query.get(resultado_id)

def update_resultado(resultado_id, data):
    """
    Atualiza um resultado existente.

    :param resultado_id: Identificador do resultado a ser atualizado.
    :param data: Dicionário contendo os novos dados do resultado.
    :return: O resultado atualizado.
    """
    resultado = Resultado.query.get(resultado_id)
    if resultado:
        resultado.corrida_id = data['corrida_id']
        resultado.piloto_id = data['piloto_id']
        resultado.posicao = data['posicao']
        db.session.commit()
    return resultado

def delete_resultado(resultado_id):
    """
    Deleta um resultado pelo seu identificador.

    :param resultado_id: Identificador do resultado a ser deletado.
    """
    resultado = Resultado.query.get(resultado_id)
    if resultado:
        db.session.delete(resultado)
        db.session.commit()
