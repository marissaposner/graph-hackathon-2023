from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from helpers.schemas import NFT_Marketplace
documents = SimpleDirectoryReader('docs').load_data()
index = GPTSimpleVectorIndex(documents)

# response = index.query("""You are an AI that helps write GraphQL queries on the Graph Protocol. In the coming prompts I'll feed you questions that you need to turn into graphQL queries that work. Show only code and do not use sentences. Note that it's important that if you don't have some specific data (like dates or IDs), just add placeholders. Show only code and do not use sentences. 
# What is the past 24 hour volume of NFTs?""")
response = index.query("""You are an AI that helps write GraphQL queries on the Graph Protocol. In the coming prompts I'll feed you questions that you need to turn into graphQL queries that work. Show only code and do not use sentences. Note that it's important that if you don't have some specific data (like dates or IDs), just add placeholders. Show only code and do not use sentences. 
What is the average trade size of the past 24 hours?""")
print(response)
