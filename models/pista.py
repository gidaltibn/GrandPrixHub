from database import db

class Pista(db.Model):
    __tablename__ = 'pistas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    pais = db.Column(db.String(128))

    corridas = db.relationship('Corrida', back_populates='pista')

    def __repr__(self):
        return f'<Pista {self.nome}>'
