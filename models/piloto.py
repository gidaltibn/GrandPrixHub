from database import db

class Piloto(db.Model):
    __tablename__ = 'pilotos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    idade = db.Column(db.Integer)
    nacionalidade = db.Column(db.String(64))
    equipe_id = db.Column(db.Integer, db.ForeignKey('equipes.id'))
    equipe = db.relationship('Equipe', back_populates='pilotos')

    def __repr__(self):
        return f'<Piloto {self.nome}>'
