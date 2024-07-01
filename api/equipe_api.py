from flask_restx import Namespace, Resource, fields
from models.equipe import Equipe
from database import db

api = Namespace('equipes', description='Operations related to teams')

equipe_model = api.model('Equipe', {
    'id': fields.Integer(readOnly=True, description='The team identifier'),
    'nome': fields.String(required=True, description='The team name')
})

@api.route('/')
class EquipeList(Resource):
    @api.marshal_list_with(equipe_model)
    def get(self):
        equipes = Equipe.query.all()
        return equipes

    @api.expect(equipe_model)
    @api.marshal_with(equipe_model, code=201)
    def post(self):
        data = api.payload
        nova_equipe = Equipe(nome=data['nome'])
        db.session.add(nova_equipe)
        db.session.commit()
        return nova_equipe, 201

@api.route('/<int:id>')
@api.response(404, 'Equipe not found')
@api.param('id', 'The team identifier')
class EquipeResource(Resource):
    @api.marshal_with(equipe_model)
    def get(self, id):
        equipe = Equipe.query.get_or_404(id)
        return equipe

    @api.expect(equipe_model)
    @api.marshal_with(equipe_model)
    def put(self, id):
        equipe = Equipe.query.get_or_404(id)
        data = api.payload
        equipe.nome = data['nome']
        db.session.commit()
        return equipe

    @api.response(204, 'Equipe deleted')
    def delete(self, id):
        equipe = Equipe.query.get_or_404(id)
        db.session.delete(equipe)
        db.session.commit()
        return '', 204
