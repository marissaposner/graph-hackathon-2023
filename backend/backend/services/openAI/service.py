import openai

from backend.config import OPENAI_API_KEY
from backend.services.graph.graphql_examples import LIST_OF_EXAMPLES
from llama_index import LLMPredictor, GPTSimpleVectorIndex, SimpleDirectoryReader, PromptHelper
from llama_index.indices import GPTListIndex
from llama_index import Document


from langchain import OpenAI
from backend.services.graph import subgraphs
import os 

PRE_PROMPT = """
You are an AI that helps write GraphQL queries on the Graph Protocol. 
In the coming prompts I'll feed you questions that you need to turn into graphQL queries that work.  
Note that it's important that if you don't have some specific data (like dates or IDs), just add placeholders. 
Show only code and do not use sentences."""
def generate_prompt(input):
    """
    Take in query from user and prepend sample queries
    """
    sample_queries = LIST_OF_EXAMPLES
    return (
        sample_queries
        + f"""
You are an AI that helps write GraphQL queries on the Graph Protocol. 
In the coming prompts I'll feed you questions that you need to turn into graphQL queries that work.  
Note that it's important that if you don't have some specific data (like dates or IDs), just add placeholders. 
Show only code and do not use sentences. 
{input}
"""
    )


class OpenAIService:
    def __init__(self, use_prompt=0):
        openai.api_key = OPENAI_API_KEY

<<<<<<< HEAD

  def request_gql_for_graph_2(self, input_query):
    """
    testing new chatgpt api"""
    PATH = os.getcwdb().decode("utf-8") + "/subgraphs/subgraphs/aave-governance/"
    with open(PATH+"schema.graphql"):
    # documents = SimpleDirectoryReader(list(PATH+"schema.graphql")).load_data()
    # documents = [Document(t) for t in PATH]
    # documents = SimpleDirectoryReader(input_files = list(PATH + "schema.graphql")).load_data()
    # print("documents", documents)
    # index = GPTSimpleVectorIndex(documents)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": """You are an AI that helps write GraphQL queries on the Graph Protocol. 
            In the coming prompts I'll feed you questions that you need to turn into graphQL queries that work. 
            Show only code and do not use sentences. Note that it's important that if you don't have some specific data 
            (like dates or IDs), just add placeholders. Show only code and do not use sentences.{}""".format(input_query)}]
        )
    print("completion['choices'][0]['message']['content']", completion['choices'][0]['message']['content'])
    return completion['choices'][0]['message']['content']

  def request_gql_for_graph(self, input_query):
    # path = "/subgraphs/subgraphs/" #TODO UPDATE
    # PATH = os.path.dirname(os.path.dirname(path))
    
    # with os.scandir(os.getcwdb().decode("utf-8") + PATH) as p:
    #   for entry in p:
    #           # only consider directories that arent prefixed by a dot or underscore
    #           if not entry.name.startswith((".", "_")) and not entry.is_file():
    #               print(entry)
    PATH = os.getcwdb().decode("utf-8") + "/subgraphs/subgraphs/aave-governance/"

    # with open(PATH+"schema.graphql"):
    # documents = open(PATH+"schema.graphql")
    # print(type(documents))

    documents = SimpleDirectoryReader(PATH).load_data()
    for d in documents: print(d)
    # except:
    #     PATH = os.getcwdb().decode("utf-8") + "/subgraphs/subgraphs/aave-governance/schema.graphql"
    #     documents = SimpleDirectoryReader.load_data(input_files=list(PATH)).load_data()
    
    index = GPTSimpleVectorIndex(documents)
    # save to disk
    index.save_to_disk('index.json')
    # load from disk
    # index = GPTSimpleVectorIndex.load_from_disk('index.json')
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

=======
    def request_gql_for_graph(self, input_query, subgraph, generic=False):
        prompt = input_query if generic else generate_prompt(input_query)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(input_query),
            temperature=0.6,
            max_tokens=2048,
        )
        openai_result = response.choices[0].text
        print("==========openai response:==========\n", openai_result)
        # strip any unnecessary text prepended and/or postpended to the gql query
        openai_result = openai_result[
            openai_result.find("{") : openai_result.rfind("}") + 1
        ]
        print("==========openai response (formatted):==========\n", openai_result)
        return openai_result
>>>>>>> d5fb5828a514db32411aef7b160dfb2e6477d55c
