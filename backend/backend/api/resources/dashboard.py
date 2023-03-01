from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from backend.api.schemas import UserSchema
from backend.models import User
from backend.extensions import db
from backend.commons.pagination import paginate
from backend.controllers.api.v1 import APIV1Controller

DEFAULT_INPUT = "What proposal has the most votes?"

class DashboardCreator(Resource):
    """Dashboard Resource
    """
    # to enable security uncomment line below
    # method_decorators = [jwt_required()]

    def get(self, input_sentence):

        print("=========== input_sentence ===============")
        print(input_sentence)
        print("=========== input_sentence ===============")

        controller = APIV1Controller()
        response = controller.handle_query_for_dashboard(input_sentence)
        print(response)
        return response



    def post(self):
        try:
            input_sentence = request.get_json().get("input")
            if input_sentence == "":
                raise
        except:
            input_sentence = DEFAULT_INPUT

        print("=========== input_sentence ===============")
        print(input_sentence)
        print("=========== input_sentence ===============")

        controller = APIV1Controller()
        response = controller.handle_query_for_dashboard(input_sentence)
        print(response)
        return response
