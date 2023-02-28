import os
import requests

from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env.
api_key = os.getenv("THEGRAPH_API_KEY")


def query_thegraph(subgraph_id, query, hosted=True):
    if hosted:
        base_url = "https://api.thegraph.com/subgraphs/name/"
    else:
        base_url = f"https://gateway.thegraph.com/api/{api_key}/subgraphs/id/"
    query_url = f"{base_url}{subgraph_id}"
    r = requests.post(query_url, json={"query": query})
    r.raise_for_status()
    try:
        # assumes only one table is being queried
        first_table_name = list(r.json()["data"].keys())[0]
        return r.json()["data"][first_table_name]
    except KeyError:
        print(r.json())


def merge_graph_queries(column_to_merge: str):
    """combine the results"""
    # I want to compare the volume to another
    # every type of question has a diff column to merge
    # teach gpt what a comparison is
