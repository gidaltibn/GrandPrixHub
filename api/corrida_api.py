from flask_restx import Namespace, Resource, fields
from models.corrida import Corrida
from database import db
from datetime import datetime

api = Namespace('corrida', description='Operações relacionadas às corridas')

corrida_model = api.model('Corrida', {
    'id': fields.Integer(readOnly=True, description='Identificador da corrida'),
    'nome': fields.String(required=True, description='Nome da corrida'),
    'data_corrida': fields.String(required=True, description='Data da corrida'),  # Mantém como string para receber JSON
    'pista_id': fields.Integer(required=True, description='Identificador da pista')
})

@api.route('/')
class CorridaList(Resource):
    @api.marshal_list_with(corrida_model)
    def get(self):
        corridas = Corrida.query.all()
        return corridas

    @api.expect(corrida_model)
    @api.marshal_with(corrida_model, code=201)
    def post(self):
        data = api.payload
        data_corrida = datetime.strptime(data['data_corrida'], '%Y-%m-%d').date()  # Converte string para date
        nova_corrida = Corrida(
            nome=data['nome'],
            data_corrida=data_corrida,
            pista_id=data['pista_id']
        )
        db.session.add(nova_corrida)
        db.session.commit()
        return nova_corrida, 201

@api.route('/<int:id>')
@api.response(404, 'Corrida não encontrada')
@api.param('id', 'Identificador da corrida')
class CorridaResource(Resource):
    @api.marshal_with(corrida_model)
    def get(self, id):
        corrida = Corrida.query.get_or_404(id)
        return corrida

    @api.expect(corrida_model)
    @api.marshal_with(corrida_model)
    def put(self, id):
        corrida = Corrida.query.get_or_404(id)
        data = api.payload
        corrida.nome = data.get('nome', corrida.nome)
        corrida.data_corrida = datetime.strptime(data['data_corrida'], '%Y-%m-%d').date()  # Converte string para date
        corrida.pista_id = data.get('pista_id', corrida.pista_id)
        db.session.commit()
        return corrida

    @api.response(204, 'Corrida excluída')
    def delete(self, id):
        corrida = Corrida.query.get_or_404(id)
        db.session.delete(corrida)
        db.session.commit()
        return '', 204
