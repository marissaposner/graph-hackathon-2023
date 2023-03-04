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
}"""), 
Prompt(
q="What are the 5 biggest transactions?",
o="""query{
  transfers(orderBy: value, orderDirection: desc, first: 5) {
    value
    transactionHash
  }
}"""),
Prompt(
q="What is the biggest transaction?",
o="""query{
  transfers(orderBy: value, orderDirection: desc, first: 1) {
    value
    transactionHash
  }
}""")

]
