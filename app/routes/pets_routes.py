from flask import Blueprint
from app.controllers import pets_controllers


bp = Blueprint("pets", __name__, url_prefix="/pets")


bp.get("")(pets_controllers.get_all_pets)
bp.get("/<int:pet_id>")(pets_controllers.get_pets_by_id)
bp.post("")(pets_controllers.create_pets)
bp.patch("/<int:pet_id>")(pets_controllers.atualizando_pets)
bp.delete("/<int:pet_id>")(pets_controllers.delete_pet_by_id)