import os
import requests

import pandas as pd
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


def main():
    # eg https://thegraph.com/hosted-service/subgraph/messari/erc20-holders-2022
    json_result = query_thegraph(
        "messari/erc20-holders-2022",
        """
            query {
                tokens(first: 5) {
                    id
                    name
                    symbol
                    decimals
                }
            }
        """,
        "tokens",
    )
    print(pd.DataFrame(json_result))

    # eg https://thegraph.com/explorer/subgraphs/G1F2huam7aLSd2JYjxnofXmqkQjT5K2fRjdfapwiik9c?view=Overview&chain=mainnet
    json_result = query_thegraph(
        "G1F2huam7aLSd2JYjxnofXmqkQjT5K2fRjdfapwiik9c",
        """
            query {
                marketplaces(first: 5) {
                    id
                    name
                    slug
                    network
                }
            }
        """,
        "marketplaces",
        hosted=False,
    )
    print(pd.DataFrame(json_result))


if __name__ == "__main__":
    main()
