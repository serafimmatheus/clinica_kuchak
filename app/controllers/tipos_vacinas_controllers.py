from http import HTTPStatus
from flask import current_app, jsonify, request, session
from app.models.tipos_vacinas_model import TiposVacinasModel
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from flask_jwt_extended import jwt_required


@jwt_required()
def craete_vacinas():
    session: Session = current_app.db.session
    data = request.get_json()


    if data["is_pupies"]:
        td = timedelta(21)

        vacinas_data = {
            "nome": data["nome"],
            "data_aplicacao": data["data_aplicacao"],
            "data_revacinacao": datetime.strptime(data["data_aplicacao"], '%d/%m/%Y') + td,
            "is_pupies": data["is_pupies"],
            "pet_id": data["pet_id"]
        }

        vacinas = TiposVacinasModel(**vacinas_data)

        session.add(vacinas)
        session.commit()

        return jsonify(vacinas), HTTPStatus.CREATED


    td = timedelta(365)

    vacinas_data = {
        "nome": data["nome"],
        "data_aplicacao": data["data_aplicacao"],
        "data_revacinacao": datetime.strptime(data["data_aplicacao"], '%d/%m/%Y') + td,
        "is_pupies": data["is_pupies"],
        "pet_id": data["pet_id"]
    }

    vacinas = TiposVacinasModel(**vacinas_data)


    session.add(vacinas)
    session.commit()

    return jsonify(vacinas), HTTPStatus.CREATED


@jwt_required()
def get_all_vacinas():
    session: Session = current_app.db.session

    vacinas = session.query(TiposVacinasModel).all()

    return jsonify(vacinas), HTTPStatus.OK


@jwt_required()
def get_vacinas_by_id(vacina_id):
    session: Session = current_app.db.session

    vacinas = session.query(TiposVacinasModel).get(vacina_id)

    if not vacinas:
        return {"message": f"id {vacina_id} not found!"}, HTTPStatus.NOT_FOUND

    return jsonify(vacinas), HTTPStatus.OK


@jwt_required()
def update_vacinas(vacina_id):
    session: Session = current_app.db.session

    data: dict = request.get_json()

    vacina = session.query(TiposVacinasModel).get(vacina_id)

    if not vacina:
        return {"message": f"id {vacina_id} not found!"}, HTTPStatus.NOT_FOUND

    for key, value in data.items():
        setattr(vacina, key, value)

    session.commit()

    return jsonify(vacina)


@jwt_required()
def delete_vacinas(vacina_id):
    session: Session = current_app.db.session

    vacina = session.query(TiposVacinasModel).get(vacina_id)

    if not vacina:
        return {"message": f"id {vacina_id} not found!"}, HTTPStatus.NOT_FOUND

    session.delete(vacina)
    session.commit()

    return "", HTTPStatus.NO_CONTENT