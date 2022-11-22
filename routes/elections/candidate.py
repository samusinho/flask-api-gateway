from flask import request, jsonify, Blueprint
import requests
from settings import VOTES_URL

candidate_bp = Blueprint("candidate_blueprint", __name__)


@candidate_bp.route("", methods=["POST"])
def create_candidate():
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url=f"{VOTES_URL}/candidates",  # localhost:5000/parties (ms votaciones)
        json=body,
        headers=headers
    )
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:  # status_code == 500
        return jsonify({
            "message": "Hubo un error al crear candidato"
        }), 500


@candidate_bp.route("", methods=["GET"])
def parties():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/candidates",  # localhost:5000/parties (ms votaciones)
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:  # status_code == 500
        return jsonify({
            "message": "Hubo un error al obtener la lista de candidatos"
        }), 500
