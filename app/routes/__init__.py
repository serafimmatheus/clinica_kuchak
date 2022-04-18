from flask import Flask, Blueprint
from app.routes.users_routes import bp as bp_users
from app.routes.clientes_routes import bp as bp_clientes
from app.routes.pets_routes import bp as bp_pets
from app.routes.tipos_vacinas_routes import bp as bp_vacinas
from app.routes.login_routes import bp as bp_login


bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_users)
    bp_api.register_blueprint(bp_clientes)
    bp_api.register_blueprint(bp_pets)
    bp_api.register_blueprint(bp_vacinas)
    bp_api.register_blueprint(bp_login)
    app.register_blueprint(bp_api)
