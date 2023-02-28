import os

import openai
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from helpers.graphql_examples import LIST_OF_EXAMPLES
from helpers.subgraphs import protocols
from helpers.thegraph import query_thegraph


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

cors = CORS(app)


@app.route("/get-thegraph-results", methods=["POST", "GET"])
@cross_origin()
def eip_subgraph_info():
    try:
        input_sentence = request.get_json()["input"]
        if input_sentence == "":
            raise
    except:
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
    # hardcode protocol and chain for now
    protocol = "makerdao"
    chain = "ethereum"
    schema_file = protocols[protocol]["schema_file"]
    protocol_type = protocols[protocol]["type"]
    if "decentralized-network" in protocols[protocol]["deployments"][chain]:
        service_type = "decentralized-network"
    else:
        service_type = "hosted-service"
    query_id = protocols[protocol]["deployments"][chain][service_type]["query-id"]
    data = query_thegraph(
        query_id,
        openai_result,
        hosted=(service_type == "hosted-service"),
    )
    print("==========the graph response:==========\n", data)
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
