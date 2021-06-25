from src import db

import json

class Skill(db.Model):
    __tablename__ = 'skill'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return json.dumps({ "id": self.id, "name": self.name, })