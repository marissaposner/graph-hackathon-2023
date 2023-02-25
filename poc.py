import requests

import pandas as pd


query = """
query {
  tokenContracts(orderBy: numOwners, orderDirection: desc, first: 10) {
    id
    name
    numTokens
    numOwners
    supportsEIP721Metadata
  }
}
"""


def main():
    subgraph = "https://api.thegraph.com/subgraphs/name/wighawag/eip721-subgraph"

    r = requests.post(subgraph, json={"query": query})
    r.raise_for_status()
    print(r.json())
    df = pd.DataFrame(r.json()["data"]["tokenContracts"])
    print(df)


if __name__ == "__main__":
    main()
