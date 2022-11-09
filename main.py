from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import requests

from settings import URL, PORT, SECURITY_URL
from routes.elections.party import party_bp
from routes.security.user import user_bp
from routes.security.authentication import authentication_bp

app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=["GET"])
def ping():
    return jsonify({
        "message": "pong..."
    })


app.register_blueprint(party_bp, url_prefix ="/parties")
app.register_blueprint(user_bp, url_prefix ="/users")
app.register_blueprint(authentication_bp, url_prefix="/authentication")

EXCLUDED_URLS = ["/", "/authentication/login"]

@app.before_request
def middleware():
    if request.path not in EXCLUDED_URLS:
        token = request.headers.get("Authorization")
        if token:
            response = validate_permissions(token, clean_path(request.path), request.method)
            if response.status_code == 200:
                return jsonify(response.json()), response.status_code
        else:
            return make_response(jsonify({
                "message": "Al parecer no has inicado sesión"
            })), 401


def validate_permissions(token, url, method):
    headers = {
        "Content-Type": "application/json",
        "Authorization": token
    }
    response = requests.post(
        url=f"{SECURITY_URL}/permissions-roles/verify",
        headers=headers,
        json={
            "url": url,
            "method": method
        }
    )
    return response

def clean_path(path):
    parts = path.split("/")
    return parts[3]



if __name__ == "__main__":
    app.run(
        debug=True,
        port=PORT,
        host=URL
    )
