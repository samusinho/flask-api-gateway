from flask import Flask, jsonify
from flask_cors import CORS
import requests
from settings import URL, PORT
from routes.elections.party import party_bp
from routes.security.user import user_bp

app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=["GET"])
def ping():
    return jsonify({
        "message": "pong..."
    })

app.register_blueprint(party_bp, url_prefix ="/parties")
app.register_blueprint(user_bp, url_prefix ="/users")




EXCLUDED_URLS = ["/", "/login"]

# @app.before_request
# def middleware():
#     if request.path not in EXCLUDED_URLS:
#         token = request.headers.get("Authorization")
#         if token:
#             pass
#         else:
#             responseObject = {
#                 "message": "Al parecer no has inicado sesión"
#             }
#             return make_response(jsonify(responseObject)), 401


if __name__ == "__main__":
    app.run(
        debug=True,
        port=PORT,
        host=URL
    )
