import datetime as dt

import requests

from backend.config import THEGRAPH_API_KEY
from backend.services.graph.subgraphs import SubgraphService


DEFAULT_PROTOCOL = "aave-governance"
DEFAULT_CHAIN = "ethereum"


def query_thegraph(subgraph_id, query, hosted=True):
    if hosted:
        base_url = "https://api.thegraph.com/subgraphs/name/messari/"
    else:
        base_url = f"https://gateway.thegraph.com/api/{THEGRAPH_API_KEY}/subgraphs/id/"
    query_url = f"{base_url}{subgraph_id}"
    r = requests.post(query_url, json={"query": query})
    r.raise_for_status()
    try:
        # assumes only one table is being queried
        first_table_name = list(r.json()["data"].keys())[0]
        return r.json()["data"][first_table_name]
    except KeyError:
        print(r.json())


class GraphService:
    def __init__(self, protocol=DEFAULT_PROTOCOL, chain=DEFAULT_CHAIN):
        self.subgraph = SubgraphService(protocol, chain)

    def query_thegraph(self, gql):
        data = query_thegraph(
            self.subgraph.query_id,
            gql,
            hosted=(self.subgraph.service_type == "hosted-service"),
        )
        print("==========the graph response:==========\n", data)
        for dict_item in data:
            for key, val in dict_item.items():
                if key == "timestamp":
                    # print(dt.datetime.utcfromtimestamp(int(val)).strftime('%Y-%m-%d %H:%M:%S'))
                    dict_item[key] = dt.datetime.utcfromtimestamp(int(val)).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
        print("formatted data", data)
        return data

    def whitelist(self):
        # TODO: generate list of protocols that can be queried
        # this will populate the dropdown in the f/e
        pass
