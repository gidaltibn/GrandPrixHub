from database import db

class Corrida(db.Model):
    __tablename__ = 'corridas'

    # Definição das colunas da tabela corridas
    id = db.Column(db.Integer, primary_key=True)  # Identificador da corrida
    nome = db.Column(db.String(128), nullable=False)  # Nome da corrida
    data_corrida = db.Column(db.Date)  # Data da corrida
    pista_id = db.Column(db.Integer, db.ForeignKey('pistas.id'))  # Chave estrangeira para a pista
    pista = db.relationship('Pista', back_populates='corridas')  # Relacionamento com a tabela pistas
    resultados = db.relationship('Resultado', back_populates='corrida')  # Relacionamento com a tabela resultados

    def __repr__(self):
        # Representação da classe Corrida
        return f'<Corrida {self.nome}>'
