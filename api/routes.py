from flask_restx import Api, Resource, fields
from models.equipe import Equipe
from database import db

# Removendo o Blueprint e iniciando o Api diretamente
api = Api(title='GrandPrixHub API', version='1.0', description='A simple API for managing teams')

ns = api.namespace('equipes', description='Operations related to teams')

equipe_model = api.model('Equipe', {
    'id': fields.Integer(readOnly=True, description='The team identifier'),
    'nome': fields.String(required=True, description='The team name')
})

@ns.route('/')
class EquipeList(Resource):
    @ns.marshal_list_with(equipe_model)
    def get(self):
        equipes = Equipe.query.all()
        return equipes

    @ns.expect(equipe_model)
    @ns.marshal_with(equipe_model, code=201)
    def post(self):
        data = api.payload
        nova_equipe = Equipe(nome=data['nome'])
        db.session.add(nova_equipe)
        db.session.commit()
        return nova_equipe, 201

@ns.route('/<int:id>')
@ns.response(404, 'Equipe not found')
@ns.param('id', 'The team identifier')
class EquipeResource(Resource):
    @ns.marshal_with(equipe_model)
    def get(self, id):
        equipe = Equipe.query.get_or_404(id)
        return equipe

    @ns.expect(equipe_model)
    @ns.marshal_with(equipe_model)
    def put(self, id):
        equipe = Equipe.query.get_or_404(id)
        data = api.payload
        equipe.nome = data['nome']
        db.session.commit()
        return equipe

    @ns.response(204, 'Equipe deleted')
    def delete(self, id):
        equipe = Equipe.query.get_or_404(id)
        db.session.delete(equipe)
        db.session.commit()
        return '', 204
