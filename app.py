from flask import Flask, request, jsonify
from flask_cors import CORS

from create_embeddings import answer_question_for_value

app = Flask(__name__)
CORS(app)

@app.route("/api")
def get_info():
    args = request.args
    app_name = args.get("app_name")
    value = args.get("value")
    eula = open(f"eulas/{app_name}.txt").read()
    return jsonify({ 'data': answer_question_for_value(app_name, value, eula) })
