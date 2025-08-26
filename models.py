from app import db

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    has_wifi = db.Column(db.Boolean, default=False)
    has_coffee = db.Column(db.Boolean, default=False)