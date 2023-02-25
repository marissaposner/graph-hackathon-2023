import os
import requests

from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env.
api_key = os.getenv("THEGRAPH_API_KEY")


def query_thegraph(subgraph_id, query, table_name, hosted=True):
    if hosted:
        base_url = "https://api.thegraph.com/subgraphs/name/"
    else:
        base_url = f"https://gateway.thegraph.com/api/{api_key}/subgraphs/id/"
    query_url = f"{base_url}{subgraph_id}"
    r = requests.post(query_url, json={"query": query})
    r.raise_for_status()
    return r.json()["data"][table_name]
