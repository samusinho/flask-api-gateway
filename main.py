from flask import Flask, jsonify
from flask_cors import CORS
from settings import URL, PORT

app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=["GET"])
def ping():
    return jsonify({
        "message": "pong..."
    })


if __name__ == "__main__":
    app.run(
        debug=True,
        port=PORT,
        host=URL
    )
