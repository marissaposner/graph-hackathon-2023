LIST_OF_EXAMPLES = """Here are a set of example questions and queries you can use as an example for making your own queries:
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
    "Questions": "What NFT collections have the most revenue?",
    "Output": "query {
                collections(orderBy: totalRevenueETH, orderDirection: desc) {
                  id
                  name
                  symbol
                  totalRevenueETH
                }
              }",
    "Explanation": "Queries the highest revenue collections in ETH."
  },
  {
    "Questions": "What is the aave proposal with the most votes?",
    "Output": "query MostVotedProposal {
                proposals(orderBy: totalWeightedVotes, orderDirection: desc, first: 1 ) {
                  id
                  totalWeightedVotes
                }
              }",
    "Explanation": "Query the aave governance subgraph and find the proposal with the most votes."
  },
  {
    "Questions": "Show me the last 10 proposals on aave",
    "Output": "query {
  proposals(orderBy: creationTime, orderDirection: desc, first: 1) {
    id
    description
    state
    proposer {
      id
    }
    forWeightedVotes
    againstWeightedVotes
    abstainWeightedVotes
    totalWeightedVotes
    creationTime
    startBlock
    endBlock
    queueTime
    executionETA
    executionTime
    cancellationTime
  }
}
",
    "Explanation": "Show me the most recent 10 proposals on aave."
  },
  {
    "Questions": "Count the votes for and against the last 10 aave proposals",
    "Output": "query {
  proposals(orderBy: creationTime, orderDirection: desc, first: 10) {
    forWeightedVotes
    againstWeightedVotes
  }
}
",
    "Explanation": "How many people voted for and against the last 10 aave proposals?s"
  },
]
"""
