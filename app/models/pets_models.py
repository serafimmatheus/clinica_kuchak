from dataclasses import dataclass
from app.configs.database import db


@dataclass
class PetsModel(db.Model):
    __tablename__ = "pets"

    id: int
    raca: str
    nome: str
    data_nascimento: str
    vacinas: list

    id = db.Column(db.Integer, primary_key=True)
    raca = db.Column(db.String(30), nullable=False)
    nome = db.Column(db.String(30), nullable=False)
    data_nascimento = db.Column(db.Date)
    cliente_id = db.Column(db.String, db.ForeignKey("clientes.cpf"), nullable=False)
    
    vacinas = db.relationship("TiposVacinasModel", back_populates="pet_vacina")
    pet = db.relationship("ClientesModel", back_populates="pets")
