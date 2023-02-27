import os

import openai
import datetime as dt
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from helpers.thegraph import query_thegraph
from helpers.graphql_examples import LIST_OF_EXAMPLES

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

cors = CORS(app)


@app.route("/get-thegraph-results", methods=["POST", "GET"])
@cross_origin()
def eip_subgraph_info():
    try:
        input_sentence = request.get_json()["input"]
    except:
        # if there is no input sentance and we are just testing
        input_sentence = "find the date that the most NFTs in the otherside collection (0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258) were traded?"
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
    print(type(data))
    return jsonify(data)


def generate_prompt(input):
    """
    Take in query from user and prepend sample queries
    """
    sample_queries = LIST_OF_EXAMPLES
    return (
        sample_queries
        + f"""
Query: Using the above queries, Write a GraphQL query to find: {input}
Results:"""
    )
