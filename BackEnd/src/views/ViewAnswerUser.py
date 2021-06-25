from flask import Blueprint, request, jsonify
from datetime import datetime
from src import db

from src.controller.Authenticate import jwt_required
from src.controller.ValidateFieldsRequest import ValidateFieldsRequest
from src.controller.serializers.answer_serializer import Answer_Serializer

from src.model.answer_user import Answer_User
from src.model.sprint import Sprint
from src.model.user import User

import jwt, json

validate = ValidateFieldsRequest()
answer_serializer = Answer_Serializer()

bp = Blueprint('answers', __name__, url_prefix='/answers')

@bp.route('/registerAnswer', methods=['POST'])
@jwt_required
def registerAnswer(current_user):
    validateFields = validate.validateAll(['id_user_answer', 'id_sprint', 'id_answer', 'created_at'], request)
    if not validateFields['status']:
        return jsonify({ "erro": validateFields['dataField'] }), 405
    try:
        dataNow = datetime.now().strftime('%d/%m/%Y')
        data = request.json['data']

        for resposta in data:
            answer = Answer_User(
                id_user_owner=current_user.id, 
                id_user_answer=request.json['id_user_answer'],
                id_sprint=request.json['id_sprint'],
                id_answer=request.json['id_answer'],
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
def getAllAnswerBySprint(current_user):
    id_sprint = request.args.get("id_sprint")
    sprint = Sprint.query.filter_by(id=id_sprint).first()
    try:
        if sprint:
            role_current_user = current_user.role

            if role_current_user == 'master':
                data = answer_serializer.serializerAllBySprint(id_sprint)
                return jsonify(data)
            
            else:
                return jsonify({ "status": "Voce nao possui acesso a essa transação" })

        else:
            return jsonify({"erro": "sprint nao encontrada"}),404

    except Exception as e: 
        error = { 'erro': f'{e}' }
        return jsonify(error), 500

@bp.route('/getAnswerByUser', methods=['GET'])
@jwt_required
def getAnswerByUser(current_user):
    id_user = request.args.get("id_user")
    user = User.query.filter_by(id=id_user).first()

    try:
        if user:
            role_current_user = current_user.role

            if role_current_user == 'master':
                data = answer_serializer.serializerByUser(id_user)
                return jsonify(data)

            else:
                return jsonify({ "status": "Voce nao possui acecsso a essa transação" })

        else:
            return jsonify({ "Erro": "Usuario nao encontrado" }),404

    except Exception as e: 
        error = { 'erro': f'{e}' }
        return jsonify(error), 500