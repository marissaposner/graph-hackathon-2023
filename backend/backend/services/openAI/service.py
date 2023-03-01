import openai

from backend.config import OPENAI_API_KEY

class OpenAIService:
  def __init__(self, use_prompt=0):
    openai.api_key = OPENAI_API_KEY

  def execute_request(self, input_query):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(input_query),
        temperature=0.6,
        max_tokens=2048,
    )


def generate_prompt(input):
    """
    Take in query from user and prepend sample queries
    """
    sample_queries = LIST_OF_EXAMPLES
    return (
        sample_queries
        + f"""
Query: Using the above queries, Write a GraphQL query to find: {input}
Results:"""
    )
