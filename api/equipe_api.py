from flask_restx import Namespace, Resource, fields
from models.equipe import Equipe
from database import db

api = Namespace('equipes', description='Operações relacionadas às equipes')

equipe_model = api.model('Equipe', {
    'id': fields.Integer(readOnly=True, description='Identificador da equipe'),
    'nome': fields.String(required=True, description='Nome da equipe')
})

@api.route('/')
class EquipeList(Resource):
    @api.marshal_list_with(equipe_model)
    def get(self):
        """Lista todas as equipes"""
        equipes = Equipe.query.all()
        return equipes

    @api.expect(equipe_model)
    @api.marshal_with(equipe_model, code=201)
    def post(self):
        """Cria uma nova equipe"""
        data = api.payload
        nova_equipe = Equipe(nome=data['nome'])
        db.session.add(nova_equipe)
        db.session.commit()
        return nova_equipe, 201

@api.route('/<int:id>')
@api.response(404, 'Equipe não encontrada')
@api.param('id', 'O identificador da equipe')
class EquipeResource(Resource):
    @api.marshal_with(equipe_model)
    def get(self, id):
        """Obtém uma equipe pelo seu identificador"""
        equipe = Equipe.query.get_or_404(id)
        return equipe

    @api.expect(equipe_model)
    @api.marshal_with(equipe_model)
    def put(self, id):
        """Atualiza uma equipe pelo seu identificador"""
        equipe = Equipe.query.get_or_404(id)
        data = api.payload
        equipe.nome = data['nome']
        db.session.commit()
        return equipe

    @api.response(204, 'Equipe deletada')
    def delete(self, id):
        """Deleta uma equipe pelo seu identificador"""
        equipe = Equipe.query.get_or_404(id)
        db.session.delete(equipe)
        db.session.commit()
        return '', 204
