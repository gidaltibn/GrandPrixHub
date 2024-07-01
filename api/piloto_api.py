from flask_restx import Namespace, Resource, fields
from models.piloto import Piloto
from database import db

api = Namespace('piloto', description='Operations related to pilots')

piloto_model = api.model('Piloto', {
    'id': fields.Integer(readOnly=True, description='The pilot identifier'),
    'nome': fields.String(required=True, description='The pilot name'),
    'idade': fields.Integer(description='The pilot age'),
    'nacionalidade': fields.String(description='The pilot nationality'),
    'equipe_id': fields.Integer(description='The team ID')
})

@api.route('/')
class PilotoList(Resource):
    @api.marshal_list_with(piloto_model)
    def get(self):
        pilotos = Piloto.query.all()
        return pilotos

    @api.expect(piloto_model)
    @api.marshal_with(piloto_model, code=201)
    def post(self):
        data = api.payload
        novo_piloto = Piloto(nome=data['nome'], idade=data['idade'], nacionalidade=data['nacionalidade'], equipe_id=data['equipe_id'])
        db.session.add(novo_piloto)
        db.session.commit()
        return novo_piloto, 201

@api.route('/<int:id>')
@api.response(404, 'Piloto not found')
@api.param('id', 'The pilot identifier')
class PilotoResource(Resource):
    @api.marshal_with(piloto_model)
    def get(self, id):
        piloto = Piloto.query.get_or_404(id)
        return piloto

    @api.expect(piloto_model)
    @api.marshal_with(piloto_model)
    def put(self, id):
        piloto = Piloto.query.get_or_404(id)
        data = api.payload
        piloto.nome = data.get('nome', piloto.nome)
        piloto.idade = data.get('idade', piloto.idade)
        piloto.nacionalidade = data.get('nacionalidade', piloto.nacionalidade)
        piloto.equipe_id = data.get('equipe_id', piloto.equipe_id)
        db.session.commit()
        return piloto

    @api.response(204, 'Piloto deleted')
    def delete(self, id):
        piloto = Piloto.query.get_or_404(id)
        db.session.delete(piloto)
        db.session.commit()
        return '', 204
