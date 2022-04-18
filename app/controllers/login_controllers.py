from http import HTTPStatus
from flask import current_app, request
from sqlalchemy.orm import Session, Query
from app.models.usuarios_models import UsuarioModel
from flask_jwt_extended import create_access_token


def login():
    session: Session = current_app.db.session

    data = request.get_json()

    email: UsuarioModel = session.query(UsuarioModel).filter_by(email=data["email"]).first()

    if not email:
        return {"error": f"User not found"}, HTTPStatus.NOT_FOUND


    if email.verify_password(data["password"]):
        access_token = create_access_token(identity=email)
        return {"token": access_token, "data": email}, HTTPStatus.OK
    else:
        return {"error": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
