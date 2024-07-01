from database import db

class Resultado(db.Model):
    __tablename__ = 'resultados'

    id = db.Column(db.Integer, primary_key=True)
    corrida_id = db.Column(db.Integer, db.ForeignKey('corridas.id'), nullable=False)
    primeiro_lugar_id = db.Column(db.Integer, db.ForeignKey('pilotos.id'), nullable=False)
    segundo_lugar_id = db.Column(db.Integer, db.ForeignKey('pilotos.id'), nullable=False)
    terceiro_lugar_id = db.Column(db.Integer, db.ForeignKey('pilotos.id'), nullable=False)

    corrida = db.relationship('Corrida', back_populates='resultados')
    primeiro_lugar = db.relationship('Piloto', foreign_keys=[primeiro_lugar_id])
    segundo_lugar = db.relationship('Piloto', foreign_keys=[segundo_lugar_id])
    terceiro_lugar = db.relationship('Piloto', foreign_keys=[terceiro_lugar_id])

    def __repr__(self):
        return f'<Resultado {self.id}>'
