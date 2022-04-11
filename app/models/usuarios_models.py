from dataclasses import dataclass
from app.configs.database import db


@dataclass
class UsuarioModel(db.Model):
    __tablename__ = "usuarios"

    id:int
    nome: str
    img_url: str
    email: str
    clientes: list

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    img_url = db.Column(db.String)
    email = db.Column(db.String(100), nullable=False, unique=True)
    clientes = db.relationship("ClientesModel", back_populates="users")
