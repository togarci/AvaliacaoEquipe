from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash
from src import db
import datetime, jwt

from src.model.user import User
from src.model.user_groups import User_Groups
from src.controller.ValidateFieldsRequest import ValidateFieldsRequest

validate = ValidateFieldsRequest()

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/register', methods=['POST'])
def registerUser():
    validateFields = validate.validateAll([ 'name', 'email', 'password', 'role' ], request)
    if not validateFields['status']:
        return jsonify({ "erro": validateFields['dataField'] }), 405
    
    id_groups = User_Groups.query.filter_by(group_name=request.json['role']).first()

    try:
        if id_groups:
            user = User(
                name=request.json['name'],
                fk_id_user_group=id_groups.id, 
                email=request.json['email'], 
                password=request.json['password']
            )
            
            db.session.add(user)
            db.session.commit()

            payload = {
                "id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            
            token = jwt.encode(payload, current_app.config['SECRET_KEY'])
            
            data = { "id_user": f'{user.id}', "status": "cadastro efetuado", "token": f'{token.decode("utf-8")}' }

            return jsonify(data)

        else:
            return jsonify({ "erro": "voce errou feio, errou rude !" })

    except Exception as e: 
        error = { 'erro': f'{e}' }
        return jsonify(error), 500


@bp.route('/login', methods=['POST'])
def login():
    validateFields = validate.validateAll([ 'email', 'password' ], request)
    if not validateFields['status']:
        return Response('{"Error": %r }' % validateFields['dataField'], mimetype="application/json", status=405)
    
    try:
        email = request.json['email']
        password = request.json['password']
        
        user = User.query.filter_by(email=email).first()
        if user:
            if not user.verify_password(password):
                return jsonify({ "error": "password is wrong" }), 403
            payload = {
                "id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=15)
            }
            token = jwt.encode(payload, current_app.config['SECRET_KEY'])
           
            return jsonify({ "id_user": user.id, "email": user.email, "token": f'{token.decode("utf-8") }', "status": "LogIn Efetuado" })
        else:
            return jsonify({ "error": "email not found"}), 404
       
    except Exception as e:
        error = { 'erro': f'{e}' }
        return jsonify({ "error": error })