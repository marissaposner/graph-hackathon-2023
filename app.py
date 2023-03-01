import os
import openai
import datetime as dt
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from helpers.graphql_examples import LIST_OF_EXAMPLES
from helpers.schemas import NFT_Marketplace
from helpers.subgraphs import protocols
from helpers.thegraph import query_thegraph
from helpers.schemas import NFT_Marketplace
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
        # if there is no input sentence and we are just testing
        input_sentence = "What proposal has the most votes?"
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
    protocol = "aave-governance"
    chain = "ethereum"
    # schema_file = protocols[protocol]["schema_file"]
    # protocol_type = protocols[protocol]["type"]
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
    for dict_item in data:
        for key, val in dict_item.items():
            if key == "timestamp":
                # print(dt.datetime.utcfromtimestamp(int(val)).strftime('%Y-%m-%d %H:%M:%S'))
                dict_item[key] = dt.datetime.utcfromtimestamp(int(val)).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
    return jsonify(data)


def generate_prompt(input):
    """
    Take in query from user and prepend sample queries
    """
    # sample_queries = LIST_OF_EXAMPLES
    schema = NFT_Marketplace
    return (
        f""" 
You are an AI that helps write GraphQL queries on the Graph Protocol. In the coming prompts I'll feed you questions that you need to turn into graphQL queries that work. Show only code and do not use sentences. Note that it's important that if you don't have some specific data (like dates or IDs), just add placeholders. Show only code and do not use sentences. 
Using the above queries, Write a GraphQL query to: {input}
""" + schema 
    )
