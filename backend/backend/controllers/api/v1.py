import openai

from backend.services.openAI.service import OpenAIService
from backend.services.graph.service import GraphService


class APIV1Controller:
    def handle_query_for_dashboard(self, input_sentence):
        """Get data for query

        Parameters
        ----------
        input_sentence : _type_
        """
        ai_service = OpenAIService()
        gql = ai_service.request_gql_for_graph(input_sentence)
        graph_service = GraphService()
        result = graph_service.query_thegraph(gql)
        import pdb
        pdb.set_trace()
