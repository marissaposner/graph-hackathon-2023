CHAT = """
give 50 names for chat bot that generates a dashboard for blockchain data
"""

from backend.services.openAI.service import OpenAIService

ai = OpenAIService()
ai.request_gql_for_graph(CHAT, generic=True)
