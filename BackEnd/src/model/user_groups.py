from src import db
import json

class User_Groups(db.Model):
    __tablename__ = 'user_groups'
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(30), nullable=False)    

    def __init__(self, group_name=None):
        self.group_name = group_name
        

    def __repr__(self):
       return json.dumps({"id": self.id, "group_name": self.group_name })