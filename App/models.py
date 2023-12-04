from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(60), nullable=False)
    usuario_id = db.Column(db.String(20), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)

























