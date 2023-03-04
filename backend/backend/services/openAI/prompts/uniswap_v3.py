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
        }
        """,
    ),
]
