from flask import Blueprint, request, jsonify, current_app
import jwt

from src.model.question import Question
from src.controller.ValidateFieldsRequest import ValidateFieldsRequest
from src.controller.Authenticate import jwt_required
from src.controller.serializers.question_serializer import Question_Serializer

validate = ValidateFieldsRequest()
question_serializer = Question_Serializer()

bp = Blueprint('questions', __name__, url_prefix='/questions')

@bp.route('/getAllQuestions', methods=['GET'])
@jwt_required
def getAllQuestions(current_user):
    try:
        data = question_serializer.serializerAll()
        return jsonify(data)
    
    except Exception as e: 
        error = { 'erro': f'{e}' }
        return jsonify(error), 500

@bp.route('/getQuestionById', methods=['GET'])
@jwt_required
def getQuestionById(current_user):
    try:
        id = request.args.get("id")
        data = question_serializer.serializerById(id)
        return jsonify(data)
    
    except Exception as e: 
        error = { 'erro': f'{e}' }
        return jsonify(error), 500