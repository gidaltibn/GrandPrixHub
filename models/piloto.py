from database import db

class Piloto(db.Model):
    __tablename__ = 'pilotos'

    # Definição das colunas da tabela pilotos
    id = db.Column(db.Integer, primary_key=True)  # Identificador do piloto
    nome = db.Column(db.String(128), nullable=False)  # Nome do piloto
    idade = db.Column(db.Integer)  # Idade do piloto
    nacionalidade = db.Column(db.String(64))  # Nacionalidade do piloto
    equipe_id = db.Column(db.Integer, db.ForeignKey('equipes.id'))  # Chave estrangeira para a tabela equipes
    equipe = db.relationship('Equipe', back_populates='pilotos')  # Relacionamento com a tabela equipes

    def __repr__(self):
        # Representação da classe Piloto
        return f'<Piloto {self.nome}>'
