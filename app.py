from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from database import db
from api.equipe_api import api as equipe_ns
from api.piloto_api import api as piloto_ns
from api.corrida_api import api as corrida_ns
from api.pista_api import api as pista_ns
from api.resultado_api import api as resultado_ns

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grandprixhub.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    CORS(app)

    db.init_app(app)

    # Registrando namespaces diretamente com a API
    from api.api import api
    api.init_app(app)

    # Inicializando as namespaces individuais
    api.add_namespace(equipe_ns)
    api.add_namespace(piloto_ns)
    api.add_namespace(corrida_ns)
    api.add_namespace(pista_ns)
    api.add_namespace(resultado_ns)

    with app.app_context():
        #db.drop_all()
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
