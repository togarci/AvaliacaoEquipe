from src import db
from src.model.type_skill import Type_Skill
import json

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    fk_id_type_skill = db.Column(db.Integer, db.ForeignKey('type_skill.id'), nullable=False)

    def __init__(self, question=None, fk_id_type_skill=None):
        self.question = question
        self.fk_id_type_skill = fk_id_type_skill

    def __repr__(self):
        return json.dumps({ "id": self.id, "question": self.question, "fk_id_type_skill": self.fk_id_type_skill })