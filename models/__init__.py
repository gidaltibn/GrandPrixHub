from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Criar a instância do db aqui

from .equipe import Equipe  # Garantir que as classes dos modelos são importadas depois de db
