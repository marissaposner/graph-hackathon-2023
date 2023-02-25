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


@app.route("/")
def home():
    return "Hello World"
