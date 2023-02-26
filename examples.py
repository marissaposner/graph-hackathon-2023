import pandas as pd

from helpers.thegraph import query_thegraph


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
                }
        """,
        "collectionDailySnapshots",
        hosted=False,
    )
    print(pd.DataFrame(json_result))


if __name__ == "__main__":
    main()
