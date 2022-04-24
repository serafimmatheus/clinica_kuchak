from http import HTTPStatus
from flask import current_app, jsonify, request
from sqlalchemy.orm import Session
from app.models.cats_models import CatsModel
from app.models.clientes_models import ClientesModel
from app.models.usuarios_models import UsuarioModel
from flask_jwt_extended import get_jwt_identity, jwt_required


def create_cats():
    session: Session = current_app.db.session
    data: dict = request.get_json()

    try:
        cat = CatsModel(**data)

        session.add(cat)
        session.commit()

        return jsonify(cat), HTTPStatus.CREATED

    except TypeError:
        esperado = ["raca", "nome", "data_nascimento", "pelagem", "is_castrado", "is_testado", "cliente_id"]
        obtido = [key for key in data.keys()]

        return {"esperado": esperado, "obtido": obtido}, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_all_cats():
    session: Session = current_app.db.session

    user_auth = get_jwt_identity()

    cats = session.query(CatsModel).select_from(CatsModel).join(ClientesModel).join(UsuarioModel).where(UsuarioModel.id == user_auth["id"]).all()

    if not cats:
        return jsonify([]), HTTPStatus.OK

    return jsonify(cats), HTTPStatus.OK


@jwt_required()
def get_cats_by_id(id: int):
    session: Session = current_app.db.session

    user_auth = get_jwt_identity()

    cats = session.query(CatsModel).select_from(CatsModel).join(ClientesModel).join(UsuarioModel).where(UsuarioModel.id == user_auth["id"]).all()

    list_cats = []
    for cat in cats:
        if cat.id == id:
            list_cats.append(cat)

    if not list_cats:
        return jsonify({"error": "gatinho não encontrado!"}), HTTPStatus.NOT_FOUND


    return jsonify(list_cats[0]), HTTPStatus.OK


@jwt_required()
def update_cats_by_id(id: int):
    return {"msg": "update"}


@jwt_required()
def delete_cats_by_id(id: int):
    return {"msg": "delete"}

    