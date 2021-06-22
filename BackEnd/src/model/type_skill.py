from src import db
import json

class Type_Skill(db.Model):
    __tablename__ = 'type_skill'
    id = db.Column(db.Integer, primary_key=True)
    type_skill = db.Column(db.String, nullable=False)

    def __init__(self, type_skill=None):
        self.type_skill = type_skill

    def __repr__(self):
        return json.dumps({ "id": self.id, "type_skill": self.type_skill })