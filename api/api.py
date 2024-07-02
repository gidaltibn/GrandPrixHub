from flask_restx import Api

api = Api(
    title='GrandPrixHub API',
    version='1.0',
    description='Uma API simples para gerenciar times, pilotos, pistas, corridas e resultados da F1.'
)
