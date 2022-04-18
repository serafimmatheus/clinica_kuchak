from http import HTTPStatus
from flask import current_app, jsonify, request
from sqlalchemy.orm import Session
from app.models.clientes_models import ClientesModel
from flask_jwt_extended import jwt_required


@jwt_required()
def create_clientes():
    session: Session = current_app.db.session

    data: dict = request.get_json()

    cliente = ClientesModel(**data)

    session.add(cliente)
    session.commit()

    return jsonify(cliente), HTTPStatus.CREATED


@jwt_required()
def get_all_clientes():
    session: Session = current_app.db.session

    page = request.args.get("page", 1)
    per_page = request.args.get("per_page", 5)

    clientes = session.query(ClientesModel).paginate(page=int(page), per_page=int(per_page))

    return jsonify(clientes.items), HTTPStatus.OK


@jwt_required()
def get_clientes_by_id(cliente_cpf: str):
    session: Session = current_app.db.session

    try:
        clientes = session.query(ClientesModel).get(cliente_cpf)
        return jsonify(clientes), HTTPStatus.OK
    except:
        return {"message": f"id {cliente_cpf} not found!"}, HTTPStatus.NOT_FOUND


@jwt_required()
def atualizando_clientes(cliente_cpf: str):
    session: Session = current_app.db.session

    data: dict = request.get_json()

    cliente_find_cpf = session.query(ClientesModel).filter_by(cpf=cliente_cpf).first()

    for key, value in data.items():
        setattr(cliente_find_cpf, key, value)

    session.commit()

    return jsonify(cliente_find_cpf), HTTPStatus.OK


@jwt_required()
def delete_clientes(cliente_cpf: str):
    session: Session = current_app.db.session

    cliente_find_cpf = session.query(ClientesModel).filter_by(cpf=cliente_cpf).first()

    session.delete(cliente_find_cpf)
    session.commit()

    return "", HTTPStatus.NO_CONTENT



