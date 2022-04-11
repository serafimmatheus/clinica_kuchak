from http import HTTPStatus
from flask import jsonify, request, current_app, session
from app.models.usuarios_models import UsuarioModel
from sqlalchemy.orm import Session


def create_users():
    session: Session = current_app.db.session
    data = request.get_json()

    usuarios = UsuarioModel(**data)

    session.add(usuarios)
    session.commit()

    return jsonify(usuarios), HTTPStatus.CREATED


def get_all_users():
    session: Session = current_app.db.session
    page = request.args.get("page", 1)
    per_page = request.args.get("per_page", 5)
    users = session.query(UsuarioModel).paginate(page=int(page), per_page=int(per_page))

    return jsonify(users.items)


def get_user_by_id(user_id: int):
    session: Session = current_app.db.session
    user_find_id = session.query(UsuarioModel).get(user_id)

    return jsonify(user_find_id), HTTPStatus.OK


def update_users(user_id: int):
    session: Session = current_app.db.session

    data: dict = request.get_json() 
    user = session.query(UsuarioModel).get(user_id)

    for key, value in data.items():
        setattr(user, key, value)

    session.commit()

    return jsonify(user), HTTPStatus.OK


def delete_user(user_id: int):
    session: Session = current_app.db.session

    user = session.query(UsuarioModel).get(user_id)

    session.delete(user)
    session.commit()

    return "", HTTPStatus.NO_CONTENT


