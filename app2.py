import os

import openai
from flask import Flask, jsonify

from thegraph import query_thegraph


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/get-thegraph-results", methods=["POST", "GET"])
def eip_subgraph_info():
    data = query_thegraph(
        "messari/erc20-holders-2022",
        """
            query {
                tokens(orderBy: transferCount, first: 5, orderDirection: desc) {
                    id
                    name
                    symbol
                    decimals
                    transferCount
                }
            }
        """,
        "tokens",
    )
    return jsonify({"Results": data})


<<<<<<< HEAD:app2.py
Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )


def send_schema_to_gpt(schema):
    """Define the schema of the subgraph to send to gpt
    """
=======
@app.route("/")
def home():
    return "Hello World"
>>>>>>> 68e1ae6b3ba28b2e0d90bce1917cad62b9e28535:app.py
