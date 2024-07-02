from database import db

class Resultado(db.Model):
    __tablename__ = 'resultados'

    # Definição das colunas da tabela resultados
    id = db.Column(db.Integer, primary_key=True)  # Identificador do resultado
    corrida_id = db.Column(db.Integer, db.ForeignKey('corridas.id'), nullable=False)  # Identificador da corrida
    primeiro_lugar_id = db.Column(db.Integer, db.ForeignKey('pilotos.id'), nullable=False)  # Identificador do piloto em primeiro lugar
    segundo_lugar_id = db.Column(db.Integer, db.ForeignKey('pilotos.id'), nullable=False)  # Identificador do piloto em segundo lugar
    terceiro_lugar_id = db.Column(db.Integer, db.ForeignKey('pilotos.id'), nullable=False)  # Identificador do piloto em terceiro lugar

    # Relacionamentos com as tabelas corridas e pilotos
    corrida = db.relationship('Corrida', back_populates='resultados')
    primeiro_lugar = db.relationship('Piloto', foreign_keys=[primeiro_lugar_id])
    segundo_lugar = db.relationship('Piloto', foreign_keys=[segundo_lugar_id])
    terceiro_lugar = db.relationship('Piloto', foreign_keys=[terceiro_lugar_id])

    def __repr__(self):
        # Representação da classe Resultado
        return f'<Resultado {self.id}>'
