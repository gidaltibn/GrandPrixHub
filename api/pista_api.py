from flask_restx import Namespace, Resource, fields
from models.pista import Pista
from database import db

api = Namespace('pista', description='Operações relacionadas às pistas')

pista_model = api.model('Pista', {
    'id': fields.Integer(readOnly=True, description='Identificador da pista'),
    'nome': fields.String(required=True, description='Nome da pista'),
    'pais': fields.String(required=True, description='País onde a pista está localizada')
})

@api.route('/')
class PistaList(Resource):
    @api.marshal_list_with(pista_model)
    def get(self):
        """Lista todas as pistas"""
        pistas = Pista.query.all()
        return pistas

    @api.expect(pista_model)
    @api.marshal_with(pista_model, code=201)
    def post(self):
        """Cria uma nova pista"""
        data = api.payload
        nova_pista = Pista(nome=data['nome'], pais=data['pais'])
        db.session.add(nova_pista)
        db.session.commit()
        return nova_pista, 201

@api.route('/<int:id>')
@api.response(404, 'Pista não encontrada')
@api.param('id', 'Identificador da pista')
class PistaResource(Resource):
    @api.marshal_with(pista_model)
    def get(self, id):
        """Obtém uma pista pelo seu identificador"""
        pista = Pista.query.get_or_404(id)
        return pista

    @api.expect(pista_model)
    @api.marshal_with(pista_model)
    def put(self, id):
        """Atualiza uma pista pelo seu identificador"""
        pista = Pista.query.get_or_404(id)
        data = api.payload
        pista.nome = data.get('nome', pista.nome)
        pista.pais = data.get('pais', pista.pais)
        db.session.commit()
        return pista

    @api.response(204, 'Pista excluída')
    def delete(self, id):
        """Deleta uma pista pelo seu identificador"""
        pista = Pista.query.get_or_404(id)
        db.session.delete(pista)
        db.session.commit()
        return '', 204
