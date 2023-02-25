import pandas as pd

from thegraph import query_thegraph


def main():
    # # eg https://thegraph.com/hosted-service/subgraph/messari/erc20-holders-2022
    # json_result = query_thegraph(
    #     "messari/erc20-holders-2022",
    #     """
    #         query {
    #             tokens(orderBy: transferCount, first: 5, orderDirection: desc) {
    #                 id
    #                 name
    #                 symbol
    #                 decimals
    #                 transferCount
    #             }
    #         }
    #     """,
    #     "tokens",
    # )
    # print(pd.DataFrame(json_result))

    # # eg https://thegraph.com/explorer/subgraphs/G1F2huam7aLSd2JYjxnofXmqkQjT5K2fRjdfapwiik9c?view=Overview&chain=mainnet
    json_result = query_thegraph(
        "AwoxEZbiWLvv6e3QdvdMZw4WDURdGbvPfHmZRc8Dpfz9",
        """
            query {
                CollectionDailySnapshot(
                    where: {token1: "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"},
                    orderBy: dailyTradedItemCount,
                    orderDirection: desc,
                    first: 1,
                ) {
                    dailyTradedItemCount
                    date
                }
            }
        """,
        "CollectionDailySnapshot",
        hosted=False,
    )
    print(pd.DataFrame(json_result))


if __name__ == "__main__":
    main()
