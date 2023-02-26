import os

import openai
from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_cors import CORS, cross_origin
from schemas import NFT_Marketplace
from thegraph import query_thegraph


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

schema = NFT_Marketplace

cors = CORS(app)
@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


@app.route("/get-thegraph-results", methods=["POST", "GET"])
@cross_origin()
def eip_subgraph_info():
    input_sentence = request.get_json()["input"]
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
    return jsonify(data)


def generate_prompt(input):
    schema = send_schema_to_gpt()
    return (
        schema
        + """   Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
            input.capitalize()
        )
    )


def send_schema_to_gpt(schema):
    """Define the schema of the subgraph to send to gpt"""
    return NFT_Marketplace
