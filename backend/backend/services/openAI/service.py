import openai

from backend.config import OPENAI_API_KEY
from backend.services.graph.graphql_examples import LIST_OF_EXAMPLES
from llama_index import LLMPredictor, GPTSimpleVectorIndex, SimpleDirectoryReader, PromptHelper
from llama_index.indices import GPTListIndex


from langchain import OpenAI
from backend.services.graph import subgraphs
import os 
def generate_prompt(input):
    """
    Take in query from user and prepend sample queries
    """
    sample_queries = LIST_OF_EXAMPLES
    return (
        sample_queries
        + f"""
You are an AI that helps write GraphQL queries on the Graph Protocol. In the coming prompts I'll feed you questions that you need to turn into graphQL queries that work. Show only code and do not use sentences. Note that it's important that if you don't have some specific data (like dates or IDs), just add placeholders. Show only code and do not use sentences. 
{input}
"""
    )


class OpenAIService:
  def __init__(self, use_prompt=0):
    openai.api_key = OPENAI_API_KEY

  def request_gql_for_graph(self, input_query):
    # path = "/subgraphs/subgraphs/" #TODO UPDATE
    # PATH = os.path.dirname(os.path.dirname(path))
    
    # with os.scandir(os.getcwdb().decode("utf-8") + PATH) as p:
    #   for entry in p:
    #           # only consider directories that arent prefixed by a dot or underscore
    #           if not entry.name.startswith((".", "_")) and not entry.is_file():
    #               print(entry)
    
    try:
        PATH = os.getcwdb().decode("utf-8") + "/subgraphs/subgraphs/aave-governance/"
        documents = SimpleDirectoryReader(PATH).load_data()
    except:
        PATH = os.getcwdb().decode("utf-8")[0:-8] + "/subgraphs/subgraphs/aave-governance/schema.graphql"
        documents = SimpleDirectoryReader.load_data(input_files=list(PATH)).load_data()
    index = GPTSimpleVectorIndex(documents)

    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003"))

    # define prompt helper
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_output = 256
    # set maximum chunk overlap
    max_chunk_overlap = 20
    prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)

    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )

    # response = index.query("""You are an AI that helps write GraphQL queries on the Graph Protocol. In the coming prompts I'll feed you questions that you need to turn into graphQL queries that work. Show only code and do not use sentences. Note that it's important that if you don't have some specific data (like dates or IDs), just add placeholders. Show only code and do not use sentences. 
    # What is the total trading volume by tier?""")
    response = index.query("""You are an AI that helps write GraphQL queries on the Graph Protocol. 
    In the coming prompts I'll feed you questions that you need to turn into graphQL queries that work. 
    Show only code and do not use sentences. Note that it's important that if you don't have some specific data 
    (like dates or IDs), just add placeholders. Show only code and do not use sentences.
    {}""".format(input_query))
    print(response)
    # response = openai.Completion.create(
    #   model="text-davinci-003",
    #   prompt=generate_prompt(input_query),
    #   temperature=0.6,
    #   max_tokens=2048,
    # )
    #   import pdb;pdb.set_trace()
    openai_result = response.response
    print("==========openai response:==========\n", openai_result)
    # openai_result = response.choices[0].text
    # print("==========openai response:==========\n", openai_result)
    return openai_result

