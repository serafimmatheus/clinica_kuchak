from http import HTTPStatus
from flask import current_app, jsonify, request, session
from sqlalchemy.orm import Session
from app.models.pets_models import PetsModel
from app.models.usuarios_models import UsuarioModel
from app.models.clientes_models import ClientesModel
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def create_pets():
    session: Session = current_app.db.session

    data = request.get_json()

    pets = PetsModel(**data)

    session.add(pets)
    session.commit()

    return jsonify(pets), HTTPStatus.CREATED


@jwt_required()
def get_all_pets():
    session: Session = current_app.db.session
    user_auth = get_jwt_identity()


    cliente = session.query(ClientesModel).filter_by(user_id=user_auth["id"]).all()

    teste = []
    for i in cliente:
        pets = session.query(PetsModel).filter_by(cliente_id=i.cpf).all()
        if pets:
            teste.append(pets)

    if not teste:
        return jsonify([])

    return jsonify(teste[0]), HTTPStatus.OK


@jwt_required()
def get_pets_by_id(pet_id: int):
    session: Session = current_app.db.session

    pet_find_id = session.query(PetsModel).get(pet_id)

    return jsonify(pet_find_id)


@jwt_required()
def atualizando_pets(pet_id: int):
    session: Session = current_app.db.session

    data = request.get_json()
    pet_find = session.query(PetsModel).get(pet_id)

    for key, value in data.items():
        setattr(pet_find, key, value)

    session.commit()

    return jsonify(pet_find), HTTPStatus.OK


@jwt_required()
def delete_pet_by_id(pet_id: int):
    session: Session = current_app.db.session

    pet_find_id = session.query(PetsModel).get(pet_id)

    session.delete(pet_find_id)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
    