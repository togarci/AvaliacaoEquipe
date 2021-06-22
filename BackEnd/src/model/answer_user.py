from src.model.user import User
from src.model.question import Question
from src import db

import json

class Answer_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_id_user = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    fk_id_question = db.Column(db.Integer, db.ForeignKey("question.id"), nullable=False)
    answer = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.String(10))

    def __init__(self, fk_id_user=None, fk_id_question=None, answer=None, created_at=None):
        self.fk_id_user = fk_id_user
        self.fk_id_question = fk_id_question
        self.answer = answer
        self.created_at = created_at

    def __repr__(self):
        return json.dumps({ 
            "id": self.id,
            "fk_id_user": self.fk_id_user,
            "fk_id_question": self.fk_id_question,
            "answer": self.answer,
            "created_at": self.created_at
        })
        