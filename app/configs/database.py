from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.clientes_models import ClientesModel
    from app.models.usuarios_models import UsuarioModel
    from app.models.pets_models import PetsModel
    from app.models.tipos_vacinas_model import TiposVacinasModel
    