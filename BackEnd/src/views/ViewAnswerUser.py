from flask import Blueprint, request, jsonify
from datetime import datetime
from src import db

from src.controller.Authenticate import jwt_required
from src.controller.ValidateFieldsRequest import ValidateFieldsRequest
from src.controller.serializers.answer_serializer import Answer_Serializer

from src.model.answer_user import Answer_User
from src.model.user_groups import User_Groups

import jwt, json

validate = ValidateFieldsRequest()
answer_serializer = Answer_Serializer()

bp = Blueprint('answers', __name__, url_prefix='/answers')

@bp.route('/registerAnswer', methods=['POST'])
@jwt_required
def registerAnswer(current_user):
    try:
        dataNow = datetime.now().strftime('%d/%m/%Y')
        data = request.json['data']

        for resposta in data:
            answer = Answer_User(fk_id_user=current_user.id, 
                                fk_id_question=resposta['id_question'], 
                                answer=resposta['answer'], 
                                created_at=dataNow
                            )
            db.session.add(answer)
            db.session.commit()


        return jsonify({ "status": "suas respostas foram salvas com sucesso" })
    
    except Exception as e: 
        error = { 'erro': f'{e}' }
        return jsonify(error), 500

@bp.route('/getAllAnswer', methods=['GET'])
@jwt_required
def getAllAnswer(current_user):
    try:
        role_current_user = User_Groups.query.filter_by(id=current_user.fk_id_user_group).first()

        if role_current_user.group_name == 'Admin' or  role_current_user.group_name == 'Master':
            data = answer_serializer.serializerAll()
            return jsonify(data)
        
        else:
            return jsonify({ "status": "Voce nao possui acecsso a essa transação" })

    except Exception as e: 
        error = { 'erro': f'{e}' }
        return jsonify(error), 500

@bp.route('/getAnswerByUser', methods=['GET'])
@jwt_required
def getAnswerByUser(current_user):
    validateFields = validate.validateAll([ 'id_user' ], request)
    if not validateFields['status']:
        return jsonify({ "erro": validateFields['dataField'] }), 405
    
    try:
        role_current_user = User_Groups.query.filter_by(id=current_user.fk_id_user_group).first()

        if role_current_user.group_name == 'Admin' or role_current_user.group_name == 'Master':
            data = answer_serializer.serializerByUser(request.json['id_user'])
            return jsonify(data)

        else:
            return jsonify({ "status": "Voce nao possui acecsso a essa transação" })

    except Exception as e: 
        error = { 'erro': f'{e}' }
        return jsonify(error), 500