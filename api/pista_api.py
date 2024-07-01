from flask_restx import Namespace, Resource, fields
from models.pista import Pista
from database import db

api = Namespace('pista', description='Operatioapi related to teams')

pista_model = api.model('Pista', {
    'id': fields.Integer(readOnly=True, description='The track identifier'),
    'nome': fields.String(required=True, description='The track name'),
    'pais': fields.String(required=True, description='The country where the track is located')
})

@api.route('/')
class PistaList(Resource):
    @api.marshal_list_with(pista_model)
    def get(self):
        pistas = Pista.query.all()
        return pistas

    @api.expect(pista_model)
    @api.marshal_with(pista_model, code=201)
    def post(self):
        data = api.payload
        nova_pista = Pista(nome = data['nome'], pais = data['pais'])
        db.session.add(nova_pista)
        db.session.commit()
        return nova_pista, 201

@api.route('/<int:id>')
@api.response(404, 'Pista not found')
@api.param('id', 'The track identifier')
class PistaResource(Resource):
    @api.marshal_with(pista_model)
    def get(self, id):
        pista = Pista.query.get_or_404(id)
        return pista

    @api.expect(pista_model)
    @api.marshal_with(pista_model)
    def put(self, id):
        pista = Pista.query.get_or_404(id)
        data = api.payload
        pista.nome = data.get('nome', pista.nome)
        pista.pais = data.get('pais', pista.pais)
        db.session.commit()
        return pista

    @api.response(204, 'Pista deleted')
    def delete(self, id):
        pista = Pista.query.get_or_404(id)
        db.session.delete(pista)
        db.session.commit()
        return '', 204
