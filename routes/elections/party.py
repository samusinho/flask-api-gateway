from flask import request, jsonify, Blueprint
import requests
from settings import VOTES_URL

party_bp = Blueprint("party_blueprint", __name__)


@party_bp.route("", methods=["POST"])
def create_party():
    body = request.get_json()
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(
        url=f"{VOTES_URL}/parties",  # localhost:5000/parties (ms votaciones)
        json=body,
        headers=headers
    )
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:  # status_code == 500
        return jsonify({
            "message": "Hubo un error al crear partido político"
        }), 500


@party_bp.route("", methods=["GET"])
def parties():
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/parties",  # localhost:5000/parties (ms votaciones)
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:  # status_code == 500
        return jsonify({
            "message": "Hubo un error al obtener la lista de partidos"
        }), 500


@party_bp.route("/<string:party_id>", methods=["GET"])
def party(party_id):
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=f"{VOTES_URL}/parties/{party_id}",  # localhost:5000/parties (ms votaciones)
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:  # status_code == 500
        return jsonify({
            "message": "Hubo un error al obtener la información del partido"
        }), 500
