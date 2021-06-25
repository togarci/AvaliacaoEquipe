from src import db
from src.model.skill import Skill
import json

class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    id_skill = db.Column(db.Integer, db.ForeignKey("skill.id"), nullable=False)
    description = db.Column(db.String(20), nullable=False)


    def __init__(self, id_skill=None, description=None):
        self.id_skill = id_skill
        self.description = description

    def __repr__(self):
        return json.dumps({ "id": self.id, "id_skill": self.id_skill, "description": self.description })