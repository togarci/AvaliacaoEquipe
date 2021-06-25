from flask import Blueprint, request, jsonify, current_app
import jwt

from src.model.skill import Skill
from src.model.answer import Answer
from src.controller.ValidateFieldsRequest import ValidateFieldsRequest
from src.controller.Authenticate import jwt_required
from src.controller.serializers.skill_serializer import Skill_serializer

validate = ValidateFieldsRequest()
skill_serializer = Skill_serializer()

bp = Blueprint('default', __name__, url_prefix='/api')

@bp.route('/getAllskills', methods=['GET'])
@jwt_required
def getAllSkill(current_user):
    try:
        data = skill_serializer.serializerAll()
        return jsonify(data)
    
    except Exception as e: 
        error = { 'erro': f'{e}' }
        return jsonify(error), 500
