from http import HTTPStatus
from flask import current_app, jsonify, request, session
from sqlalchemy.orm import Session
from app.models.pets_models import PetsModel


def create_pets():
    session: Session = current_app.db.session

    data = request.get_json()

    pets = PetsModel(**data)

    session.add(pets)
    session.commit()

    return jsonify(pets), HTTPStatus.CREATED


def get_all_pets():
    session: Session = current_app.db.session

    pets = session.query(PetsModel).all()

    return jsonify(pets), HTTPStatus.OK


def get_pets_by_id(pet_id: int):
    session: Session = current_app.db.session

    pet_find_id = session.query(PetsModel).get(pet_id)

    return jsonify(pet_find_id)


def atualizando_pets(pet_id: int):
    session: Session = current_app.db.session

    data = request.get_json()
    pet_find = session.query(PetsModel).get(pet_id)

    for key, value in data.items():
        setattr(pet_find, key, value)

    session.commit()

    return jsonify(pet_find), HTTPStatus.OK


def delete_pet_by_id(pet_id: int):
    session: Session = current_app.db.session

    pet_find_id = session.query(PetsModel).get(pet_id)

    session.delete(pet_find_id)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
    