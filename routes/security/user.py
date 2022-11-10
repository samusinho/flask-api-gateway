from flask import request, jsonify, Blueprint
import requests
from settings import SECURITY_URL

user_bp = Blueprint("user_blueprint", __name__)


@user_bp.route("", methods=["GET"])
def users():
    headers = {
        "Content-Type": "application/json",
        "Authorization": request.headers.get("Authorization")
    }
    response = requests.get(
        url=f"{SECURITY_URL}/users",  # localhost:8080/users (ms seguridad)
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al obtener la información de los usuarios"
        }), 500
    else:
        return jsonify(response.json()), response.status_code


@user_bp.route("/<string:roleid>", methods=["POST"])
def create_user(roleid):
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url=f"{SECURITY_URL}/users?roleId={roleid}",
        json=body,
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al borrar usuario"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

@user_bp.route("/<string:userid>", methods=["DELETE"])
def delete_user(userid):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.delete(
        url=f"{SECURITY_URL}/users/{userid}",
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al borrar usuario"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

