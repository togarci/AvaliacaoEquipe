from src import db
from werkzeug.security import generate_password_hash, check_password_hash
from src.model.user_groups import User_Groups
import json

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fk_id_user_group = db.Column(db.Integer, db.ForeignKey('user_groups.id'), nullable=False)
    name = db.Column(db.String, nullable=False)    
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


    def __init__(self, name=None, fk_id_user_group=None, email=None, password=None):
        self.name = name
        self.fk_id_user_group = fk_id_user_group
        self.email = email
        self.password = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
       return json.dumps({"id": self.id, "name": self.name, "email": self.email, "password": self.password})