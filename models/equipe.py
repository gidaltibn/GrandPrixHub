from database import db

class Equipe(db.Model):
    __tablename__ = 'equipes'

    # Definição das colunas da tabela equipes
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Identificador da equipe
    nome = db.Column(db.String(128), nullable=False)  # Nome da equipe
    pilotos = db.relationship('Piloto', back_populates='equipe')  # Relacionamento com a tabela pilotos

    def __repr__(self):
        # Representação da classe Equipe
        return f'<Equipe {self.nome}>'
