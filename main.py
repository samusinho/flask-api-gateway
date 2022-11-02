from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from settings import URL, PORT, VOTES_URL, SECURITY_URL

app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=["GET"])
def ping():
    return jsonify({
        "message": "pong..."
    })


@app.route("/parties", methods=["POST"])  # localhost:5001/parties (api-gateway)
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


@app.route("/parties", methods=["GET"])
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


if __name__ == "__main__":
    app.run(
        debug=True,
        port=PORT,
        host=URL
    )
