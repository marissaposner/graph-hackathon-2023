import openai

from backend.extensions import db
from backend.services.openAI.service import OpenAIService
from backend.services.graph.service import GraphService
from backend.models.dashboard import DashboardQueryResult


class APIV1Controller:
    def handle_query_for_dashboard(self, input_sentence, subgraph):
        """Get data for query

        Parameters
        ----------
        input_sentence : _type_
        """
        ai_service = OpenAIService()
        gql = ai_service.request_gql_for_graph(input_sentence, subgraph)
        graph_service = GraphService(protocol=subgraph)
        result = graph_service.query_thegraph(gql)
        dashboard_result = DashboardQueryResult(user_input=input_sentence,
                                                subgraph=subgraph,
                                                chatgpt_gql=gql,
                                                gql_valid=(result != ""))

        db.session.add(dashboard_result)
        db.session.commit()
        return result

    def get_dashboard(self, dashboard_id):
        return DashboardQueryResult.query.get(dashboard_id).to_dict()
