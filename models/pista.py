from database import db

class Pista(db.Model):
    __tablename__ = 'pistas'

    # Definição das colunas da tabela pistas
    id = db.Column(db.Integer, primary_key=True)  # Identificador da pista
    nome = db.Column(db.String(128), nullable=False)  # Nome da pista
    pais = db.Column(db.String(128))  # País onde a pista está localizada

    # Relacionamento com a tabela corridas
    corridas = db.relationship('Corrida', back_populates='pista')

    def __repr__(self):
        # Representação da classe Pista
        return f'<Pista {self.nome}>'
