from flask import Flask, jsonify, request, make_response
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
@app.route("/users/<string:roleid>", methods=["POST"])
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
    return jsonify(response.json()), 201

EXCLUDED_URLS = ["/", "/login"]

@app.before_request
def middleware():
    if request.path not in EXCLUDED_URLS:
        token = request.headers.get("Authorization")
        if token:
            pass
        else:
            responseObject = {
                "message": "Al parecer no has inicado sesión"
            }
            return make_response(jsonify(responseObject)), 401


if __name__ == "__main__":
    app.run(
        debug=True,
        port=PORT,
        host=URL
    )
