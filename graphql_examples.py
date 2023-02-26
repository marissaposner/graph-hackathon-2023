LIST_OF_EXAMPLES="""Here are a set of example questions and queries you can use as an example for making your own queries:

[
  {
    "Questions": "What date were the most NFTs in the Bored Ape NFT collection traded? ",
    "Output": "query {
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
                }",
    "Explanation": "Queries the Bored Ape NFT collection and finds the date with the highest daily trade volume in ETH. \n\nThe timestamp is the number of days since the Unix epoch (basically the Unix timestamp, divided by 86400)."
  },
  {
    "Questions": "What is the traded volume in ETH, the number of NFTs traded, and the number of collections?",
    "Output": "query {
  marketplaceDailySnapshots(orderBy: timestamp, orderDirection: desc) {
    cumulativeTradeVolumeETH
    dailyTradedItemCount
    dailyTradedCollectionCount
    timestamp
  }
}",
    "Explanation": "Query the Opensea, LooksRare, or another NFT marketplace by trade volume in ETH, number of NFTs traded, and the number of collections."
  },
  {
    "Questions": ("What NFT collections have the most revenue?", ,
    "Output": "query {
  collections(orderBy: totalRevenueETH, orderDirection: desc) {
    id
    name
    symbol
    totalRevenueETH
  }
}"
]
"""

