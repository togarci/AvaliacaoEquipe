from src import db
import json

class Sprint(db.Model):
    __tablename__ = 'sprint'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.String(10), nullable=False)
    start_date = db.Column(db.String(10), nullable=False)
    end_date = db.Column(db.String(10), nullable=False)

    def __init__(self, name=None, created_at=None, start_date=None, end_date=None):
        self.name = name
        self.created_at = created_at
        self.start_date = start_date
        self.end_date = end_date


    def __repr__(self):
       return json.dumps({"id": self.id, "name": self.name, "start_date": self.start_date, "end_data": self.end_date, "created_at": self.created_at })