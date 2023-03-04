from backend.services.openAI.graph_prompt import GraphPromptBase as Prompt


EXAMPLES = [

Prompt(
q="What are the top transactions and their senders and recipients?",
o="""query{
  transfers(orderBy: value, orderDirection: desc) {
    from
    id
    to
    value
  }
}""")

]
