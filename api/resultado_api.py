from flask_restx import Namespace, Resource, fields
from models.resultado import Resultado
from database import db

api = Namespace('resultado', description='Operations related to race results')

resultado_model = api.model('Resultado', {
    'id': fields.Integer(readOnly=True, description='The result identifier'),
    'corrida_id': fields.Integer(required=True, description='The race ID'),
    'primeiro_lugar_id': fields.Integer(required=True, description='The first place pilot ID'),
    'segundo_lugar_id': fields.Integer(required=True, description='The second place pilot ID'),
    'terceiro_lugar_id': fields.Integer(required=True, description='The third place pilot ID')
})

@api.route('/')
class ResultadoList(Resource):
    @api.marshal_list_with(resultado_model)
    def get(self):
        resultados = Resultado.query.all()
        return resultados

    @api.expect(resultado_model)
    @api.marshal_with(resultado_model, code=201)
    def post(self):
        data = api.payload
        novo_resultado = Resultado(
            corrida_id=data['corrida_id'],
            primeiro_lugar_id=data['primeiro_lugar_id'],
            segundo_lugar_id=data['segundo_lugar_id'],
            terceiro_lugar_id=data['terceiro_lugar_id']
        )
        db.session.add(novo_resultado)
        db.session.commit()
        return novo_resultado, 201

@api.route('/<int:id>')
@api.response(404, 'Resultado not found')
@api.param('id', 'The result identifier')
class ResultadoResource(Resource):
    @api.marshal_with(resultado_model)
    def get(self, id):
        resultado = Resultado.query.get_or_404(id)
        return resultado

    @api.expect(resultado_model)
    @api.marshal_with(resultado_model)
    def put(self, id):
        resultado = Resultado.query.get_or_404(id)
        data = api.payload
        resultado.corrida_id = data.get('corrida_id', resultado.corrida_id)
        resultado.primeiro_lugar_id = data.get('primeiro_lugar_id', resultado.primeiro_lugar_id)
        resultado.segundo_lugar_id = data.get('segundo_lugar_id', resultado.segundo_lugar_id)
        resultado.terceiro_lugar_id = data.get('terceiro_lugar_id', resultado.terceiro_lugar_id)
        db.session.commit()
        return resultado

    @api.response(204, 'Resultado deleted')
    def delete(self, id):
        resultado = Resultado.query.get_or_404(id)
        db.session.delete(resultado)
        db.session.commit()
        return '', 204
