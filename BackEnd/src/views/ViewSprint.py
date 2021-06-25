from flask import Blueprint, request, jsonify, current_app
import jwt

from src import db
from datetime import datetime
from src.model.sprint import Sprint
from src.controller.ValidateFieldsRequest import ValidateFieldsRequest
from src.controller.Authenticate import jwt_required
from src.controller.serializers.sprint_serializer import Sprint_serializer

validate = ValidateFieldsRequest()
sprint_serializer = Sprint_serializer()

bp = Blueprint('Sprint', __name__, url_prefix='/sprint')

@bp.route('/getAllSprints', methods=['GET'])
@jwt_required
def getAllSprints(current_user):
    try:
        data = sprint_serializer.serializerAll()
        return jsonify(data)
    
    except Exception as e: 
        error = { 'erro': f'{e}' }
        return jsonify(error), 500

@bp.route('/registerSprint', methods=['POST'])
@jwt_required
def registerSprint(current_user):
    validateFields = validate.validateAll([ 'name', 'start_date', 'end_date' ], request)
    if not validateFields['status']:
        return jsonify({ "erro": validateFields['dataField'] }), 405

    created_at = datetime.now().strftime('%d/%m/%Y')
    try:
        sprint = Sprint(
            name=request.json['name'],
            start_date=request.json['start_date'],
            end_date=request.json['end_date'],
            created_at=created_at
        )

        db.session.add(sprint)
        db.session.commit()
        
        data = sprint_serializer.serialzerSprintById(sprint.id)
        return jsonify(data)

    except Exception as e: 
        error = { 'erro': f'{e}' }
        return jsonify(error), 500