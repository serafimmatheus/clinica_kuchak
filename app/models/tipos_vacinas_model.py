from ast import Str
from dataclasses import dataclass
from email.policy import default
from app.configs.database import db


@dataclass
class TiposVacinasModel(db.Model):
    __tablename__ = "tipos_vacinas"


    id: int
    nome: Str
    data_aplicacao: str
    data_revacinacao: str #
    is_pupies: bool


    id = db.Column(db.BigInteger, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    data_aplicacao = db.Column(db.Date)
    data_revacinacao = db.Column(db.Date)
    is_pupies = db.Column(db.Boolean, default=False)
    pet_id = db.Column(db.Integer, db.ForeignKey("pets.id"), nullable=False)

    pet_vacina = db.relationship("PetsModel", back_populates="vacinas")