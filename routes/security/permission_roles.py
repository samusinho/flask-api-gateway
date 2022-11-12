from flask import request, jsonify, Blueprint
import requests
from settings import SECURITY_URL

permissions_roles_bp = Blueprint("permission_roles_blueprint", __name__)


@permissions_roles_bp.route("/<string:permission_role_id>", methods=["DELETE"])
def delete_user(permission_role_id):
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.delete(
        url=f"{SECURITY_URL}/permissions-roles/{permission_role_id}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al borrar el acceso"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

