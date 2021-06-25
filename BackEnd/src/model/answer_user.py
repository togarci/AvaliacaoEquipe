from src.model.user import User
from src.model.sprint import Sprint
from src.model.answer import Answer
from src import db

import json

class Answer_User(db.Model):
    __tablename__ = 'answer_user'
    id = db.Column(db.Integer, primary_key=True)
    id_user_owner = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    id_user_answer = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    id_sprint = db.Column(db.Integer, db.ForeignKey("sprint.id"), nullable=False)
    id_answer = db.Column(db.Integer, db.ForeignKey("answer.id"), nullable=False)
    created_at = db.Column(db.String(10))

    def __init__(self, id_user_owner=None, id_user_answer=None, id_sprint=None, id_answer=None, created_at=None):
        self.id_user_owner = id_user_owner
        self.id_user_answer = id_user_answer
        self.id_sprint = id_sprint
        self.id_answer = id_answer
        self.created_at = created_at

    def __repr__(self):
        return json.dumps({ 
            "id": self.id,
            "id_user_owner": self.id_user_owner,
            "id_user_answer": self.id_user_answer,
            "id_sprint": self.id_sprint,
            "id_answer": self.id_answer,
            "created_at": self.created_at
        })
        