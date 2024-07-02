from flask_restx import Namespace, Resource, fields
from models.piloto import Piloto
from database import db

api = Namespace('piloto', description='Operações relacionadas aos pilotos')

piloto_model = api.model('Piloto', {
    'id': fields.Integer(readOnly=True, description='Identificador do piloto'),
    'nome': fields.String(required=True, description='Nome do piloto'),
    'idade': fields.Integer(description='Idade do piloto'),
    'nacionalidade': fields.String(description='Nacionalidade do piloto'),
    'equipe_id': fields.Integer(description='Identificador da equipe')
})

@api.route('/')
class PilotoList(Resource):
    @api.marshal_list_with(piloto_model)
    def get(self):
        """Lista todos os pilotos"""
        pilotos = Piloto.query.all()
        return pilotos

    @api.expect(piloto_model)
    @api.marshal_with(piloto_model, code=201)
    def post(self):
        """Cria um novo piloto"""
        data = api.payload
        novo_piloto = Piloto(
            nome=data['nome'],
            idade=data['idade'],
            nacionalidade=data['nacionalidade'],
            equipe_id=data['equipe_id']
        )
        db.session.add(novo_piloto)
        db.session.commit()
        return novo_piloto, 201

@api.route('/<int:id>')
@api.response(404, 'Piloto não encontrado')
@api.param('id', 'Identificador do piloto')
class PilotoResource(Resource):
    @api.marshal_with(piloto_model)
    def get(self, id):
        """Obtém um piloto pelo seu identificador"""
        piloto = Piloto.query.get_or_404(id)
        return piloto

    @api.expect(piloto_model)
    @api.marshal_with(piloto_model)
    def put(self, id):
        """Atualiza um piloto pelo seu identificador"""
        piloto = Piloto.query.get_or_404(id)
        data = api.payload
        piloto.nome = data.get('nome', piloto.nome)
        piloto.idade = data.get('idade', piloto.idade)
        piloto.nacionalidade = data.get('nacionalidade', piloto.nacionalidade)
        piloto.equipe_id = data.get('equipe_id', piloto.equipe_id)
        db.session.commit()
        return piloto

    @api.response(204, 'Piloto excluído')
    def delete(self, id):
        """Deleta um piloto pelo seu identificador"""
        piloto = Piloto.query.get_or_404(id)
        db.session.delete(piloto)
        db.session.commit()
        return '', 204
