from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from backend.api.schemas import UserSchema
from backend.models import User
from backend.extensions import db
from backend.commons.pagination import paginate
from backend.controllers.api.v1 import APIV1Controller

DEFAULT_INPUT = "find the date that the most NFTs in the otherside collection (0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258) were traded?"

class DashboardCreator(Resource):
    """Dashboard Resource
    """
    # to enable security uncomment line below
    # method_decorators = [jwt_required()]

    def get(self):
        try:
            input_sentence = request.get_json().get("input", DEFAULT_INPUT)
        except:
            input_sentence = DEFAULT_INPUT
            print("using default")

        controller = APIV1Controller()
        response = controller.handle_query_for_dashboard(input_sentence)

        return {"user": "f"}
