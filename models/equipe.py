from database import db

class Equipe(db.Model):
    __tablename__ = 'equipes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(128), nullable=False)
    pilotos = db.relationship('Piloto', back_populates='equipe')

    def __repr__(self):
        return f'<Equipe {self.nome}>'
