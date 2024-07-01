from database import db

class Corrida(db.Model):
    __tablename__ = 'corridas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    data_corrida = db.Column(db.Date)
    pista_id = db.Column(db.Integer, db.ForeignKey('pistas.id'))
    pista = db.relationship('Pista', back_populates='corridas')
    resultados = db.relationship('Resultado', back_populates='corrida')

    def __repr__(self):
        return f'<Corrida {self.nome}>'
