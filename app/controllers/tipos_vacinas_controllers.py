from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.tipos_vacinas_model import TiposVacinasModel
from sqlalchemy.orm import Session, Query
from datetime import datetime, timedelta
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.clientes_models import ClientesModel
from app.models.dogs_models import DogsModel
from app.models.usuarios_models import UsuarioModel
from app.models.cats_models import CatsModel
from psycopg2.errors import ForeignKeyViolation


@jwt_required()
def craete_vacinas():
    session: Session = current_app.db.session
    data = request.get_json()

    query: Query = (
        session
        .query(TiposVacinasModel)
        .select_from(TiposVacinasModel)
        .join(CatsModel)
        .join(DogsModel)
        .join(CatsModel)
        .join(UsuarioModel)
        .where()
    )

    try:
        if data.get("pet_id"):
            if data.get("is_pupies"):
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

        if data.get("cat_id"):
            if data.get("is_pupies"):
                td = timedelta(21)

                vacinas_data = {
                    "nome": data["nome"],
                    "data_aplicacao": data["data_aplicacao"],
                    "data_revacinacao": datetime.strptime(data["data_aplicacao"], '%d/%m/%Y') + td,
                    "is_pupies": data["is_pupies"],
                    "cat_id": data["cat_id"]
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
                "cat_id": data["cat_id"]
            }

            vacinas = TiposVacinasModel(**vacinas_data)


            session.add(vacinas)
            session.commit()

            return jsonify(vacinas), HTTPStatus.CREATED


    except:
        return {"error": "esse animal nao existe!"}, HTTPStatus.NOT_FOUND


    


@jwt_required()
def get_all_vacinas():
    session: Session = current_app.db.session
    user_auth = get_jwt_identity()

    query: Query = (
        session
        .query(TiposVacinasModel)
        .select_from(TiposVacinasModel)
        .join(DogsModel)
        .join(ClientesModel)
        .join(UsuarioModel)
        .where(UsuarioModel.id == user_auth["id"]).all()
    )

    query_2: Query = (
        session
        .query(TiposVacinasModel)
        .select_from(TiposVacinasModel)
        .join(CatsModel)
        .join(ClientesModel)
        .join(UsuarioModel)
        .where(UsuarioModel.id == user_auth["id"]).all()
    )

    return jsonify(query + query_2), HTTPStatus.OK


@jwt_required()
def get_vacinas_by_id(vacina_id):
    session: Session = current_app.db.session

    user_auth = get_jwt_identity()

    try:
        query_1: Query = (
            session
            .query(TiposVacinasModel)
            .select_from(TiposVacinasModel)
            .join(DogsModel)
            .join(ClientesModel)
            .join(UsuarioModel)
            .where(UsuarioModel.id == user_auth["id"]).all()
        )

        query_2: Query = (
            session
            .query(TiposVacinasModel)
            .select_from(TiposVacinasModel)
            .join(CatsModel)
            .join(ClientesModel)
            .join(UsuarioModel)
            .where(UsuarioModel.id == user_auth["id"]).all()
        )

        query = query_1 + query_2

        list_id = []

        for i in query:
            if i.id == vacina_id:
                list_id.append(i)


        return jsonify(list_id[0])

    except IndexError:
        return {"error": f"id {vacina_id} not found!"}, HTTPStatus.NOT_FOUND



@jwt_required()
def update_vacinas(vacina_id):
    session: Session = current_app.db.session

    data: dict = request.get_json()

    user_auth = get_jwt_identity()

    try:
        vacina_1: Query = (
            session
            .query(TiposVacinasModel)
            .select_from(TiposVacinasModel)
            .join(DogsModel)
            .join(ClientesModel)
            .join(UsuarioModel)
            .where(UsuarioModel.id == user_auth["id"]).all()
        )

        vacina_2: Query = (
            session
            .query(TiposVacinasModel)
            .select_from(TiposVacinasModel)
            .join(CatsModel)
            .join(ClientesModel)
            .join(UsuarioModel)
            .where(UsuarioModel.id == user_auth["id"]).all()
        )

        vacina = vacina_1 + vacina_2

        list_id = []
        for i in vacina:
            if i.id == vacina_id:
                list_id.append(i)


        for key, value in data.items():
            setattr(list_id[0], key, value)

        session.commit()

        return jsonify(list_id[0])
    
    except IndexError:
        return {"error": "nao autorizado!"}, HTTPStatus.UNAUTHORIZED



@jwt_required()
def delete_vacinas(vacina_id):
    session: Session = current_app.db.session

    user_auth = get_jwt_identity()

    try:
        vacina_1: Query = (
            session.query(TiposVacinasModel)
            .select_from(TiposVacinasModel)
            .join(DogsModel)
            .join(ClientesModel)
            .join(UsuarioModel)
            .where(UsuarioModel.id == user_auth["id"]).all()
        )

        vacina_2: Query = (
            session.query(TiposVacinasModel)
            .select_from(TiposVacinasModel)
            .join(CatsModel)
            .join(ClientesModel)
            .join(UsuarioModel)
            .where(UsuarioModel.id == user_auth["id"]).all()
        )

        vacina = vacina_1 + vacina_2

        list_vacina = []
        for i in vacina:
            if i.id == vacina_id:
                list_vacina.append(i)

        session.delete(list_vacina[0])
        session.commit()

        return "", HTTPStatus.NO_CONTENT
    
    except IndexError:
        return {"error": "nao autorizado!"}, HTTPStatus.UNAUTHORIZED
