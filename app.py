import os

import openai
from flask import Flask, jsonify

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route('/get-Eip721-subgraph-info', methods=['POST', 'GET'])
def eip_subgraph_info():
    # data = request.get_json()
    data = {"hello": "world"}
    return jsonify({"Results": data})


@app.route('/')
def home():
    return "Hello World"
