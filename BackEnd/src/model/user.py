from src import db
from werkzeug.security import generate_password_hash, check_password_hash
import json

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(10), nullable=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


    def __init__(self, name=None, role=None, email=None, password=None):
        self.name = name
        self.role = role
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
       return json.dumps({"id": self.id, "name": self.name, "email": self.email, "password": self.password, "role": self.role})