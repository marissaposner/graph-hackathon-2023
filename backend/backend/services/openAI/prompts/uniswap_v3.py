from backend.services.openAI.graph_prompt import GraphPromptBase as Prompt


EXAMPLES = [
    Prompt(
        q="What are the top 5 USDC pools by volume?",
        o="""{
          liquidityPools(
            first: 5
            orderBy: cumulativeVolumeUSD
            orderDirection: desc
            where: {inputTokens_: {symbol: "USDC"}}
          ) {
            name
            cumulativeVolumeUSD
          }
        }""",
    ),
    Prompt(
        q="How much value is locked in the biggest pool?",
        o="""{
          liquidityPools(orderBy: totalValueLockedUSD, orderDirection: desc, first: 1) {
            name
            totalValueLockedUSD
          }
        }""",
    ),
    Prompt(
        q="How much value is locked in the biggest pool?",
        o="""{
          liquidityPools(orderDirection: asc, first: 1, orderBy: createdTimestamp) {
            name
          }
        }""",
    ),
    Prompt(
        q="What is the address for the BADGER token?",
        o="""{
          tokens(where: {symbol: "BADGER"}) {
            id
          }
        }""",
    ),
]
