import os

import openai
from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_cors import CORS, cross_origin
from schemas import NFT_Marketplace
from thegraph import query_thegraph
from graphql_examples import LIST_OF_EXAMPLES

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

schema = NFT_Marketplace

cors = CORS(app)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        input = request.form["input"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(input),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


@app.route("/get-thegraph-results", methods=["POST", "GET"])
@cross_origin()
def eip_subgraph_info():
    # input_sentence = request.get_json()["input"]
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
    """
    Take in query from user and append sample querie
    """
    sample_queries = LIST_OF_EXAMPLES
    return (
        sample_queries
        + f"""
Query: {input} 
Results:"""
    )


def define_sample_queries():
    return """Here are a set of example questions and queries you can use as an example for making your own queries:
    [
    {
        "Questions": "What date were the most NFTs in the Bored Ape NFT collection traded? ",
        "Output": "query {
                    collectionDailySnapshots(
                        where: {collection: "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"}
                        first: 1
                        orderBy: dailyTradeVolumeETH
                        orderDirection: desc
                    ) {
                        blockNumber
                        dailyTradeVolumeETH
                        timestamp
                    }
                    }",
        "Explanation": "Queries the Bored Ape NFT collection and finds the date with the highest daily trade volume in ETH. \n\nThe timestamp is the number of days since the Unix epoch (basically the Unix timestamp, divided by 86400)."
    },
    {
        "Questions": "What is the traded volume in ETH, the number of NFTs traded, and the number of collections?",
        "Output": "query {
    marketplaceDailySnapshots(orderBy: timestamp, orderDirection: desc) {
        cumulativeTradeVolumeETH
        dailyTradedItemCount
        dailyTradedCollectionCount
        timestamp
    }
    }",
        "Explanation": "Query the Opensea, LooksRare, or another NFT marketplace by trade volume in ETH, number of NFTs traded, and the number of collections."
    },
    {
        "Questions": ("What NFT collections have the most revenue?", ,
        "Output": "query {
    collections(orderBy: totalRevenueETH, orderDirection: desc) {
        id
        name
        symbol
        totalRevenueETH
    }
    }"""
# def send_schema_to_gpt(schema):
#     """Define the schema of the subgraph to send to gpt""
#     return NFT_Marketplace
