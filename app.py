import os

import openai
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from schemas import NFT_Marketplace
from thegraph import query_thegraph
from graphql_examples import LIST_OF_EXAMPLES

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

schema = NFT_Marketplace

cors = CORS(app)


@app.route("/get-thegraph-results", methods=["POST", "GET"])
@cross_origin()
def eip_subgraph_info():
    input_sentence = request.get_json()["input"]
    print("==========user response:==========\n", input_sentence)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(input_sentence),
        temperature=0.6,
        max_tokens=2048,
    )
    openai_result = response.choices[0].text
    print("==========openai response:==========\n", openai_result)
    data = query_thegraph(
        "AwoxEZbiWLvv6e3QdvdMZw4WDURdGbvPfHmZRc8Dpfz9",
        openai_result,
        "collectionDailySnapshots",
        hosted=False,
    )
    print("==========the graph response:==========\n", data)
    return jsonify(data)


def generate_prompt(input):
    """
    Take in query from user and append sample querie
    """
    sample_queries = LIST_OF_EXAMPLES
    return (
        sample_queries
        + f"""
Query: Using the above queries, Write a GraphQL query to {input}
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
