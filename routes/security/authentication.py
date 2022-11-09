from flask import request, jsonify, Blueprint
import requests
from settings import SECURITY_URL

authentication_bp = Blueprint("authentication_blueprint", __name__)

@authentication_bp.route("/login", methods=["POST"])
def login():
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url=f"{SECURITY_URL}/login",
        json=body,
        headers=headers
    )
    if response.status_code == 500:
        return jsonify({
            "message": "Hubo un error al iniciar sesión"
        }), 500
    else:
        return jsonify(response.json()), response.status_code

