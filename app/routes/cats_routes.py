from flask import Blueprint
from app.controllers import cats_controllers


bp = Blueprint("cats", __name__, url_prefix="/cats")


bp.get("")(cats_controllers.get_all_cats)
bp.get("/<int:id>")(cats_controllers.get_cats_by_id)
bp.post("")(cats_controllers.create_cats)
bp.patch("/<int:id>")(cats_controllers.update_cats_by_id)
bp.delete("/<int:id>")(cats_controllers.delete_cats_by_id)